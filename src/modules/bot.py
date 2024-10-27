"""
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2022 hunter87.dev@gmail.com
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
"""
import ast, traceback
import wavelink,requests, time
from discord.ext import commands
from wavelink import Node, Pool
from modules.chat import ChatClient
from modules import (config, payment, message_handle)
from discord import AllowedMentions, Intents, ActivityType, Activity, TextChannel, utils, Message

intents = Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True
intents.voice_states = True
intents.guilds = True
pt = time.time()
db = config.get_db()

class Spruce(commands.AutoShardedBot):
    def __init__(self) -> None:
        self.config = config
        self.chat_client = ChatClient(self)
        self.core = ("channel", "dev", "helpcog", "moderation", "music", "tourney", "role", "utils", "tasks")
        super().__init__(shard_count=config.shards, command_prefix= commands.when_mentioned_or(config.prefix),intents=intents,allowed_mentions=AllowedMentions(everyone=False, roles=False, replied_user=True, users=True),activity=Activity(type=ActivityType.listening, name="&help"))

    async def setup_hook(self) -> None:
        if config.env["tkn"] == "TOKEN":utils.setup_logging(level=30)
        self.remove_command("help")
        for i in self.core:await self.load_extension(f"core.{i}")
        nodes = [Node(uri=db.m_host, password=db.m_host_psw)]
        await Pool.connect(nodes=nodes, client=self, cache_capacity=None)

    async def on_ready(self):
        try:
            await self.tree.sync()
            stmsg = f'{self.user} | {len(self.commands)} Commands | Version : {config.version}'
            config.logger.info(stmsg)
            await config.vote_add(self)
            requests.post(url=db.cfdata.get("stwbh"), json={"content":f"<@{config.owner_id}>","embeds":[{"title":"Status","description":stmsg,"color":0xff00}]})
        except Exception as ex:print(ex)
        
    async def on_wavelink_node_ready(self, payload: wavelink.NodeReadyEventPayload) -> None:
        config.logger.info(f"Node Connected")

    async def on_disconnect(self):
        config.logger.info('Disconnected from Discord. Reconnecting...')
        await self.wait_until_ready()

    async def fetch_payment_hook(self, message:Message):
        """Fetches the payment object from the message content in paylog channel and updates the primedbc"""
        if message.channel.id != config.paylog or (not message.webhook_id): return
        try:
            obj:payment.PaymentHook = payment.PaymentHook(ast.literal_eval(message.content.replace("```", "").replace("\n", "")))
            if isinstance(obj, payment.PaymentHook) and obj.payment_status == "SUCCESS":
                return db.primedbc.update_one({"guild_id":obj.guild_id}, {"$set":obj.to_dict}, upsert=True)
            if isinstance(obj, payment.PaymentHook) and obj.payment_status == "FAILED":
                return db.paydbc.delete_one({"guild_id":obj.guild_id})
            print("Ignored the check")
        except Exception:
            traceback.print_exc()

    async def on_message(self, message:Message):
        if message.channel.id == config.paylog: await self.fetch_payment_hook(message)
        if config.notuser(message):return
        await self.process_commands(message)
        await self.chat_client.chat(message)
        if message.guild:
            await message_handle.tourney(message)
            await config.vote_check(message)
         
    async def on_command_error(self, ctx, error):
        await message_handle.error_handle(ctx, error, self)

    async def  on_guild_channel_delete(self, channel:TextChannel):
        tourch = db.dbc.find_one({"rch" : channel.id})
        dlog = self.get_channel(config.tdlog)
        if tourch:
            db.dbc.delete_one({"rch" : channel.id})
            await dlog.send(f"```json\n{tourch}\n```")

bot = Spruce()
