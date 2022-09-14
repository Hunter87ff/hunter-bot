import discord
from discord.ext import commands
from asyncio import sleep
from discord.ui import Button, View




emd = discord.Embed
helpdsk = "・__Prefix__ : `,`\n・__Total Command__ : 76 | Usable : 54\n・Type `&help <command | category>` for more information"


cmd = commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or("&"), intents=intents, help_command=None)



invbtn = Button(label="Invite", url="https://sprucebot.ml/invite")
votebtn = Button(label="Vote", url="https://discord.ly/spruce/upvote")
hel_p = "• Prefix &\n• `Total Commands` 76 | `Usable `58\n• Type `&help <command | category>` for more info\n\n"
helpemb  = discord.Embed(description=f"{hel_p}__**Categories**__\n`Music\nModeration\nUtility\nEsports\nRole`", color=0xf0ff0f)
musicemb = discord.Embed(description=f"{hel_p}__**Musics**__\n`play\npause\nresume\nstop\njoin\nleave`", color=0xff0000)
modemb   = discord.Embed(description=f"{hel_p}__**Moderation**__\n`clear, clear_perms, channel_del, channel_make, create_channel, delete_category, mute, unmute, kick, ban, hide, unhide, lock, unlock, hide_category, unhide_category, lock_category, unlock_category, setup`", color=0xff0000)
espemb   = discord.Embed(description=f"{hel_p}__**Esports**__\n`tourney_setup, add_slot, cancel_slot, group_setup, pause_tourney, start_tourney, tourney, faketag, girls_lobby`", color=0xff0000)
roleemb  = discord.Embed(description=f"{hel_p}__**Roles**__\n`create_roles, remove_roles, del_roles, give_roles, ra_role, autorole_human, autorole_bot`", color=0xff0000)
utilemb  = discord.Embed(description=f"{hel_p}__**Utility**__\n`addemoji, avatar, banner, botinfo, ping, embed, embed_img, member_count, nick, nitro, prefix, react, server_av, serverinfo, toss, userinfo, whoiss`", color=0xff0000)



class Dropdown(discord.ui.Select):
    def __init__(self):

        options = [
            discord.SelectOption(label='Main', description='Select For All Commands'),
            discord.SelectOption(label='Esports', description='Select For Tournament Commands'),
            discord.SelectOption(label='Music', description='Select For Music Commands'),
            discord.SelectOption(label='Moderation', description='Select For Noderation Commands'),
            discord.SelectOption(label='Utility', description='Select For Utility Commands'),
            discord.SelectOption(label='Role', description='Select For Role Commands'),
            #discord.SelectOption(label='Channel', description='Select For Channel Commands'),
            #discord.SelectOption(label='Greet', description='Select For Greeting Commands')
            #discord.SelectOption(label='Automod', description='Select For Automod Commands'),
        ]
        super().__init__(placeholder='Choose Command Category...', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Music":
            await interaction.response.edit_message(embed=musicemb)
        if self.values[0] == "Moderation":
            await interaction.response.edit_message(embed=modemb)
        if self.values[0] == "Esports":
            await interaction.response.edit_message(embed=espemb)
        if self.values[0] == "Main":
            await interaction.response.edit_message(embed=helpemb)
        if self.values[0] == "Utility":
            await interaction.response.edit_message(embed=utilemb)
        if self.values[0] == "Role":
            await interaction.response.edit_message(embed=roleemb)



class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())


class Helper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @bot.group(invoke_without_command=True)
    async def help(self, ctx):
        if ctx.author.bot:
            return

        opts = [invbtn, votebtn]
        view = DropdownView()
        for opt in opts:
            view.add_item(opt)
        msg = await ctx.send(embed=helpemb, view=view)



    @help.group(invoke_without_command=True)
    async def Music(self, ctx):
        view = View()
        buttons =[invbtn, votebtn]
        for bt in buttons:
            view.add_item(bt)
        await ctx.send(embed=musicemb, view=view)



    @help.group(invoke_without_command=True)
    async def Moedration(self, ctx):
        view = View()
        buttons =[invbtn, votebtn]
        for bt in buttons:
            view.add_item(bt)
        await ctx.send(embed=modemb, view=view)



    @help.group(invoke_without_command=True)
    async def Esports(self, ctx):
        view = View()
        buttons =[invbtn, votebtn]
        for bt in buttons:
            view.add_item(bt)
        await ctx.send(embed=espemb, view=view)


    @help.group(invoke_without_command=True)
    async def Role(self, ctx):
        view = View()
        buttons =[invbtn, votebtn]
        for bt in buttons:
            view.add_item(bt)
        await ctx.send(embed=roleemb, view=view)



    @help.group(invoke_without_command=True)
    async def Utility(self, ctx):
        view = View()
        buttons =[invbtn, votebtn]
        for bt in buttons:
            view.add_item(bt)
        await ctx.send(embed=utilemb, view=view)






#moderation Related

    @help.command()
    async def ban(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `ban <member>`\nExample : `&ban @abhi`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command()
    async def kick(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `kick <member>`\nExample : `&kick @abhi`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["purge"])
    async def clear(self, ctx):
        em = discord.Embed(description="Aliases : `purge`\nUsage : `clear|purge [amount=None]`\nExample : `&clear 10`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command()
    async def mute(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `mute <member> [reason=None]`\nExample : `&mute @abhi spamming`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command()
    async def unmute(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `unmute <member> [reason=None]`\nExample : `&unmute @abhi spamming`", color=0x00ff00)
        await ctx.send(embed=em)
    @help.command()
    async def setup(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `setup`\nExample : `&setup`\nNote : Mute Role Must Be Lower than My Position", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command()
    async def hide(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `hide [role=None]`\nExample : `&hide`\n", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command()
    async def unhide(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `unhide [role=None]`\nExample : `&unhide`\n", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command()
    async def lock(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `lock [role=None]`\nExample : `&lock`\n", color=0x00ff00)
        await ctx.send(embed=em)


    @help.command()
    async def unlock(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `unlock [role=None]`\nExample : `&unlock`\n", color=0x00ff00)
        await ctx.send(embed=em)




#channel Related

    @help.command(aliases=["chd"])
    async def channel_del(self, ctx):
        em = discord.Embed(description="Aliases : `chd`\nUsage : `channel_del [channels...]`\nExample : `&channel_del #general #updates`", color=0x00ff00)
        await ctx.send(embed=em)


    @help.command(aliases=["chm"])
    async def channel_make(self, ctx):
        em = discord.Embed(description="Aliases : `chm`\nUsage : `channel_make [names...]`\nExample : `&channel_make general updates`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["cch"])
    async def create_channel(self, ctx):
        em = discord.Embed(description="Aliases : `cch`\nUsage : `create_channel <category> [names...]`\nExample : `&create_channel 32745216342163 general memes announcements`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["dc"])
    async def delete_category(self, ctx):
        em = discord.Embed(description="Aliases : `dc`\nUsage : `delete_category <category>`\nExample : `&dc 7654123645287`\nDescription : `Use This Command To Delete A Hole Category | You Must Have Administrator Permission`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["hc"])
    async def hide_category(self, ctx):
        em = discord.Embed(description="Aliases : `hc`\nUsage : `hide_category <category> [role=None]`\nExample : `&hc 7654123645287`\nDescription : `Use This Command To Hide A Hole Category`", color=0x00ff00)
        await ctx.send(embed=em)     

    @help.command(aliases=["ulc"])
    async def unlock_category(self, ctx):
        em = discord.Embed(description="Aliases : `ulc`\nUsage : `unlock_category <category> [role=None]`\nExample : `&ulc 7654123645287`\nDescription : `Use This Command To unlock A Hole Category`", color=0x00ff00)
        await ctx.send(embed=em)  

    @help.command(aliases=["lc"])
    async def lock_category(self, ctx):
        em = discord.Embed(description="Aliases : `lc`\nUsage : `lock_category <category> [role=None]`\nExample : `&lc 7654123645287`\nDescription : `Use This Command To lock A Hole Category`", color=0x00ff00)
        await ctx.send(embed=em) 





#role Related
    @help.command(aliases=["croles", "crole"])
    async def create_roles(self, ctx):
        em = discord.Embed(description="Aliases : `croles`\nUsage : `create_roles [Names...]`\nExample : `&create_roles family male female`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["role", "role_give"])
    async def give_role(self, ctx):
        em = discord.Embed(description="Aliases : `role`\nUsage : `give_role <role> [users...]`\nExample : `&role @Male @hunter`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command()
    async def give_roles(self, ctx):
        em = discord.Embed(description="Aliases : `role`\nUsage : `give_roles <member> [roles...]`\nExample : `&role @hunter @male @18+`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["role_remove", "role_re"])
    async def remove_role(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `remove_role <role> [user...]`\nExample : `&remove_role @Male @hunter`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["droles", "drole"])
    async def del_roles(self, ctx):
        em = discord.Embed(description="Aliases : `croles`\nUsage : `del_roles [roles...]`\nExample : `&del_roles @group1 @group2`", color=0x00ff00)
        await ctx.send(embed=em)


    @help.command(aliases=["perms"])
    async def clear_perms(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `clear_perms [role=None]`\nExample : `&clear_perms @public`\nDescription : Use this command to remove all permissions from roles", color=0x00ff00)
        await ctx.send(embed=em)



#Esports Related

    @help.command(aliases=["add"])
    async def add_slot(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `add_slot <registration_channel> <member> <Team_Name>`\nExample : `&add_slot #register-here @ayush Team Element`\ndescription : Use This Command To Add Slot To An ongoing Tournament", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["cancel"])
    async def cancel_slot(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `cancel_slot <registration_channel> <member> [reason=None]`\nExample : `&cancel_slot #register-here @rahul abusing`\ndescription : Use This Command To Cancel A Slot Of A Tournament", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["ftf", "ft"])
    async def faketag(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `faketag <registration_channel>`\nExample : `&faketag #register-here`\ndescription : Use This Command To enable/disable Faketag Filter Of A Tournament", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=['gsetup'])
    async def group_setup(self, ctx):
        em = discord.Embed(description="Aliases : `gsetup`\nUsage : `group_setup <front> <amount>`\nExample : `&group_setup WS｜ 120`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=['grls_lobby', "girls_lby"])
    async def girls_lobby(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `girls_lobby <vc_amount>`\nExample : `&girls_lobby 12`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=['ts', "tsetup"])
    async def tourney_setup(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `tourney_setup <front> <total_slot> <mentions> <name>`\nExample : `&tourney_setup WS｜ 360 4 WEEKLY SCRIM`\nNote : You Must Have @tourney-mod Role", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=['st_tourney', "tourney_start"])
    async def start_tourney(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `start_tourney <registration_channel>`\nExample : `&start_tourney #register-here`\nNote : You Can Also Use channel_id", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=['ps_tourney', "tourney_pause"])
    async def pause_tourney(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `pause_tourney <registration_channel>`\nExample : `&pause_tourney #register-here`\nNote : You Can Also Use channel_id", color=0x00ff00)
        await ctx.send(embed=em)




#Utils Related

    @help.command()
    async def addemoji(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `addemoji <emoji>`\nExample : `&addemoji` <:vf:947194381172084767>", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["av"])
    async def avatar(self, ctx):
        em = discord.Embed(description="Aliases : `av`\nUsage : `avatar|av [user=None]`\nExample : `&av @hunter87`\ndescription : Use This Command To Get Avatar Of User", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["bnr"])
    async def banner(self, ctx):
        em = discord.Embed(description="Aliases : `bnr`\nUsage : `banner|bnr [user=None]`\nExample : `&bnr @hunter87`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["bi"])
    async def botinfo(self, ctx):
        em = discord.Embed(description="Aliases : `bi`\nUsage : `botinfo`\nDescription : `Use This Command To Get The Details About Me`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["emb"])
    async def embed(self, ctx):
        em = discord.Embed(description=f"Aliases : `emb`\nUsage : `embed <message>`\nExample : `&emb hello` {ctx.author.mention}", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["em"])
    async def embed_img(self, ctx):
        em = discord.Embed(description=f"Aliases : `em`\nUsage : `embed <image_url> <message>`\nExample : `&emb https://bit.ly/3d39vhz hello` {ctx.author.mention}", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["sav"])
    async def server_av(self, ctx):
        em = discord.Embed(description=f"Aliases : `sav`\nUsage : `server_av [server_id=None]`\nExample : `&sav`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["mc"])
    async def member_count(self, ctx):
        em = discord.Embed(description=f"Aliases : `mc`\nUsage : `member_count`\nExample : `&mc`", color=0x00ff00)
        await ctx.send(embed=em)


    @help.command(aliases=["nick_name"])
    async def nick(self, ctx):
        em = discord.Embed(description=f"Aliases : `Not Available`\nUsage : `nick <member> <new_name>`\nExample : `&nick` {ctx.author.mention} akash friend", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["ui"])
    async def userinfo(self, ctx):
        em = discord.Embed(description=f"Aliases : `ui`\nUsage : `userinfo [member=None]`\nExample : `&ui` {ctx.author.mention}", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command(aliases=["si"])
    async def serverinfo(self, ctx):
        em = discord.Embed(description=f"Aliases : `si`\nUsage : `serverinfo`\nExample : `&si`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command()
    async def whoiss(self, ctx):
        em = discord.Embed(description=f"Aliases : `Not Available`\nUsage : `whoiss <member>`\nExample : `&whoiss` {ctx.author.mention}", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command()
    async def toss(self, ctx):
        em = discord.Embed(description=f"Aliases : `Not Available`\nUsage : `toss`\nExample : `&toss`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command()
    async def nitro(self, ctx):
        em = discord.Embed(description=f"Aliases : `Not Available`\nUsage : `nitro`\nExample : `&nitro`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command()
    async def prefix(self, ctx):
        em = discord.Embed(description=f"Aliases : `Not Available`\nUsage : `prefix`\nExample : `&prefix`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command()
    async def react(self, ctx):
        em = discord.Embed(description=f"Aliases : `Not Available`\nUsage : `react <message_id> <emoji>`\nExample : `&react 7456213462634` <:vf:947194381172084767>", color=0x00ff00)
        await ctx.send(embed=em)




#Music Related
    @help.command(aliases=["p"])
    async def play(self, ctx):
        em = discord.Embed(description="Aliases : `p`\nUsage : `play <Song_name>`\nExample : `&p Faded`\nNote : You Mus Joined A VoiceChannel", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command()
    async def pause(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `pause`\nExample : `&pause`", color=0x00ff00)
        await ctx.send(embed=em)


    @help.command(aliases=["resm"])
    async def resume(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `resume`\nExample : `&resume`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command()
    async def join(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `join`\nExample : `&join`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command()
    async def leave(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `leave`\nExample : `&leave`", color=0x00ff00)
        await ctx.send(embed=em)

    @help.command()
    async def stop(self, ctx):
        em = discord.Embed(description="Aliases : `Not Available`\nUsage : `stop`\nExample : `&stop`", color=0x00ff00)
        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(Helper(bot))