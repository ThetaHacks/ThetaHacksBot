from discord.ext import commands
import discord
import random
import time
import datetime
from pytz import timezone
import pytz
from random import randrange



class CommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')

    @commands.command(name="next")
    async def next(self, ctx):
        def format(d, e=False):
            date_format='%H:%M'

            return d.strftime(date_format)

        def getDay(d):
            date_format='%m/%d'

            return d.strftime(date_format)

        tz_pst = pytz.timezone('US/Pacific')
        now = datetime.datetime.now(tz_pst).replace(tzinfo=None)
        ev = {
            "Hacking Starts":(datetime.datetime(2021, 1, 15, 0, 0),),
            "Among Us Hype Night":(datetime.datetime(2021, 1, 15, 21, 0),datetime.datetime(2021, 1, 15, 23, 0)),

            "Opening Ceremony, Team Mixer":(datetime.datetime(2021, 1, 16, 10, 0),datetime.datetime(2021, 1, 16, 11, 30)),
            "Alon Grinshpoon - Intro to AR (Workshop)":(datetime.datetime(2021, 1, 16, 12, 0),datetime.datetime(2021, 1, 16, 13, 00)),
            "Rohan Bansal - Electronics and the C Language (Workshop)":(datetime.datetime(2021, 1, 16, 14, 0),datetime.datetime(2021, 1, 16, 15, 0)),
            "Chinmayi Balasu - Networking in STEM (Speaker)":(datetime.datetime(2021, 1, 16, 16, 0),datetime.datetime(2021, 1, 16, 17, 0)),
            "Aldrin Brillante - Emoji Prediction (Workshop)":(datetime.datetime(2021, 1, 16, 18, 0),datetime.datetime(2021, 1, 16, 19, 0)),
            "Ivy Xu - Journey to Entrepreneurship (Speaker)":(datetime.datetime(2021, 1, 16, 20, 0),datetime.datetime(2021, 1, 16, 21, 0)),
            "Among Us Game Night":(datetime.datetime(2021, 1, 16, 21, 30),datetime.datetime(2021, 1, 17, 0, 0)),

            "Mr. John Smale - Building a CS Resume (Speaker)":(datetime.datetime(2021, 1, 17, 10, 0),datetime.datetime(2021, 1, 17, 11, 00)),
            "Mr. Chris Fairley - CAD with Fusion 360 (Workshop)":(datetime.datetime(2021, 1, 17, 14, 0),datetime.datetime(2021, 1, 17, 15, 00)),
            "Steven Puri (Speaker)":(datetime.datetime(2021, 1, 17, 16, 0),datetime.datetime(2021, 1, 17, 17, 00)),
            "Anshul Gupta - Intro to Web Dev (Workshop)":(datetime.datetime(2021, 1, 17, 18, 0),datetime.datetime(2021, 1, 17, 19, 00)),
            "Minecraft Hunger Games":(datetime.datetime(2021, 1, 17, 20, 30),datetime.datetime(2021, 1, 17, 23, 0)),

            "Hacking Ends":(datetime.datetime(2021, 1, 18, 8, 0),),
            "Judging":(datetime.datetime(2021, 1, 18, 8, 0),datetime.datetime(2021, 1, 18, 10, 30)),
            "Closing/Awards Ceremony":(datetime.datetime(2021, 1, 18, 11, 0),datetime.datetime(2021, 1, 18, 12, 0))}

        for e,t in ev.items():
            if len(t) == 2:
                if t[0] < now and t[1] > now:
                    embed = discord.Embed(
                        title="Current Event", description="\n**" + getDay(t[0]) + " " + format(t[0])+"-"+format(t[1], True) + " | " + e + "**\n\nZoom link: https://thetahacks.tech/zoom", color=0x00ff9d)
                    await ctx.send(embed=embed)
                    return 0

        l=-1
        for e,t in ev.items():
            l+=1
            if t[0] > now:
                c = list(ev.items())[l]
                final="\n**"
                if(len(c[1])==1):
                    final += getDay(c[1][0]) + " " + format(c[1][0], True) + "       | " + c[0]
                else:
                    final += getDay(c[1][0]) + " " + format(c[1][0])+"-"+format(c[1][1], True) + " | " + c[0]

                final += "**\n\nZoom link: https://thetahacks.tech/zoom"
                embed = discord.Embed(
                    title="Next Event", description=final, color=0x00ff9d)
                await ctx.send(embed=embed)
                return 0

        embed = discord.Embed(
            title="ThetaHacks Virtual has ended.", description="", color=0x00ff9d)
        await ctx.send(embed=embed)
        return 0


    @commands.command(name="events")
    async def events(self, ctx):
        def format(d, e=False):
            date_format='%H:%M'

            return d.strftime(date_format)

        def getDay(d):
            return int(d.strftime("%d"))-15


        ev = {"Hacking Starts":(datetime.datetime(2021, 1, 15, 0, 0),),
            "Among Us Hype Night":(datetime.datetime(2021, 1, 15, 21, 0),datetime.datetime(2021, 1, 15, 23, 0)),

            "Opening Ceremony, Team Mixer":(datetime.datetime(2021, 1, 16, 10, 0),datetime.datetime(2021, 1, 16, 11, 30)),
            "Alon Grinshpoon - Intro to AR (Workshop)":(datetime.datetime(2021, 1, 16, 12, 0),datetime.datetime(2021, 1, 16, 13, 00)),
            "Rohan Bansal - Electronics and the C Language (Workshop)":(datetime.datetime(2021, 1, 16, 14, 0),datetime.datetime(2021, 1, 16, 15, 00)),
            "Chinmayi Balasu - Networking in STEM (Speaker)":(datetime.datetime(2021, 1, 16, 16, 0),datetime.datetime(2021, 1, 16, 17, 00)),
            "Aldrin Brillante - Emoji Prediction (Workshop)":(datetime.datetime(2021, 1, 16, 18, 0),datetime.datetime(2021, 1, 16, 19, 00)),
            "Ivy Xu - Journey to Entrepreneurship (Speaker)":(datetime.datetime(2021, 1, 16, 20, 0),datetime.datetime(2021, 1, 16, 21, 00)),
            "Among Us Game Night":(datetime.datetime(2021, 1, 16, 21, 30),datetime.datetime(2021, 1, 17, 0, 0)),

            "Mr. John Smale - Building a CS Resume (Speaker)":(datetime.datetime(2021, 1, 17, 10, 0),datetime.datetime(2021, 1, 17, 11, 00)),
            "Mr. Chris Fairley - CAD with Fusion 360 (Workshop)":(datetime.datetime(2021, 1, 17, 14, 0),datetime.datetime(2021, 1, 17, 15, 00)),
            "Steven Puri (Speaker)":(datetime.datetime(2021, 1, 17, 16, 0),datetime.datetime(2021, 1, 17, 17, 00)),
            "Anshul Gupta - Intro to Web Dev (Workshop)":(datetime.datetime(2021, 1, 17, 18, 0),datetime.datetime(2021, 1, 17, 19, 00)),
            "Minecraft Hunger Games":(datetime.datetime(2021, 1, 17, 20, 30),datetime.datetime(2021, 1, 17, 23, 00)),

            "Hacking Ends":(datetime.datetime(2021, 1, 18, 8, 0),),
            "Judging":(datetime.datetime(2021, 1, 18, 8, 0),datetime.datetime(2021, 1, 18, 10, 30)),
            "Closing/Awards Ceremony":(datetime.datetime(2021, 1, 18, 11, 0),datetime.datetime(2021, 1, 18, 12, 00))}

        days = [{},{},{},{}]
        for e, t in ev.items():
            days[getDay(t[0])][e]=t



        final = "**??????1/15??????**\n"
        for e, t in days[0].items():
            if(len(t)==1):
                final += format(t[0], True) + "       | " + e
            else:
                final += format(t[0])+"-"+format(t[1], True) + " | " + e
            final += "\n"

        final += "\n"

        final += "**??????1/16??????**\n"
        for e, t in days[1].items():
            final += format(t[0])+"-"+format(t[1], True) + " | " + e
            final += "\n"

        final += "\n"

        final += "**??????1/17??????**\n"
        for e, t in days[2].items():
            final += format(t[0])+"-"+format(t[1], True) + " | " + e
            final += "\n"

        final += "\n"

        final += "**??????1/18??????**\n"
        for e, t in days[3].items():
            if(len(t)==1):
                final += format(t[0], True) + "       | " + e
            else:
                final += format(t[0])+"-"+format(t[1], True) + " | " + e
            final += "\n"

        final += "\n\n**Zoom link:** https://thetahacks.tech/zoom\n\nAll times are in PST"

        embed = discord.Embed(
            title="ThetaHacks Virtual has ended.", description="", color=0x00ff9d)
        await ctx.send(embed=embed)

    @commands.command(name="signup")
    async def signup(self, ctx):
        embed = discord.Embed(
            title="Sign Up", description="Signups for the next event coming soon!", color=0xb134eb)
        await ctx.send(embed=embed)
        
    @commands.command(name="raffle")
    async def raffle(self, ctx, roleName):
        role = discord.utils.get(ctx.guild.roles, name=roleName)
        
        l = len([member for member in ctx.guild.members if role in member.roles])
        
    
        
        if role is None:
            await ctx.send('There is no such role on this server!')
            return
        if l == 0:
            await ctx.send("Nobody has the role.")
            return
        
        randomRaffle = int(randrange(l))
        
        await ctx.send([member for member in ctx.guild.members if role in member.roles][randomRaffle].display_name)

    @commands.command(name="info")
    async def info(self, ctx):
        embed = discord.Embed(
            title="Information", description="The original ThetaHacks Virtual occurred from Jan. 15-18, 2021. But now, ThetaHacks is becoming something bigger... Stay tuned for more info! \n\nLinks:\nMore info and signups on our website: https://thetahacks.tech \n Devpost: https://thetahacks.devpost.com", color=0xc0e8f9)
        await ctx.send(embed=embed)

    @commands.command(name="ping")
    async def ping(self, ctx):
        start = time.perf_counter()
        message = await ctx.send("Ping...")
        end = time.perf_counter()
        duration = (end - start) * 1000
        await message.edit(content='Pong! {:.2f}ms'.format(duration))

    @commands.command(name="dice")
    async def dice(self, ctx, n=1):
        try:
            if n < 1 or n > 20:
                await ctx.send("Invalid arguments for command `dice`.")
            else:
                # roll N dice
                await ctx.send(" ".join(str(random.randint(1, 6)) for i in range(n)))
        except:  # error
            await ctx.send("Invalid arguments for command `dice`.")

    @commands.command(name="magic8")
    async def magic8(self, ctx):
        bm = ("It is certain.", "It is decidedly so.", "Without a doubt.", "Yes ??? definitely.", "Most likely.", "Outlook good.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.",
              "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful.")
        await ctx.send(random.choice(bm))

    @commands.command(name="help")
    async def help(self, ctx):
        embed = discord.Embed(
            title="Help", description="Valid commands:\n\n**Utility**\n`!events` - List event times and Zoom link\n`!next` - Show next event and Zoom link\n`!signup` - Signup form link\n`!info` - ThetaHacks information\n`!help` - \
                View valid commands\n`!stats` - See server statistics\n`!rules` - See server rules\n\n**Fun**\n`!kill @user`\n`!ping` - pong\n`!magic8` - \
                    Magic 8 ball\n`!dice N` - Roll N dice (1 <= N <= 10)", color=0x0027ff)
        await ctx.send(embed=embed)

    @commands.command(name="rules")
    async def rules(self, ctx):
        embed = discord.Embed(
            title="Server Rules", description="1. Do not bully or harass others. Homophobia, racism and other discrimination is not allowed. \
                Treat others the way you wish to be treated.\n\n2. Spamming, messages that do not contribute to the general conversation and \
                    non-English messages are not allowed. With this in mind, please also send content to its relevant channels.\n\n3. \
                        Excessive or toxic swearing, as well as generally distasteful or NSFW content is not allowed.\n\n4. Do not partake in \
                            activity against any Terms of Service within our community. This includes but is not limited to, the act of purchasing \
                                and selling accounts.\n\n5. Do not promote your personal material on our server without consent of a mod or admin. \
                                    If you would like to partner with us, please contact an admin.\n\n6. Discord statuses/nicknames/names should be clean, \
                                        this means no slurs, nothing that breaks TOS, no promotion, etc. Failure to comply with a mod???s request to change your \
                                            status in a timely manner will deem a punishment proportionate to how severe your status is.\n\n7. Logical extensions of \
                                                rules may also be enforced.", color=0xaa00ff)
        await ctx.send(embed=embed)

    @commands.command(name="kill")
    async def kill(self, ctx, member: discord.Member):
        if not member:
            return await ctx.send("Invalid arguments for command `kill`")
        kill_messages = ["barbecued", "disintegrated", "360-no-scoped",
                         "eaten alive", "yeeted out of existence", "squashed", "smited", "dropped in the void"]
        # choose random message
        this_msg = random.choice(kill_messages)

        embed = discord.Embed(
            title="K-O!", description="%s was %s by %s" % (member.display_name, this_msg, ctx.author.display_name), color=0xff00d1)
        await ctx.send(embed=embed)

    @commands.command(name="stats")
    async def stats(self, ctx):
        everyone = ctx.guild.get_role(717170061382516736)
        attendees = ctx.guild.get_role(721874238801313884)
        partners = ctx.guild.get_role(741822062221459568)
        bots = ctx.guild.get_role(721827685990531113)
        mentors = ctx.guild.get_role(722143200910901250)
        staff = ctx.guild.get_role(730445847938203718)
        coordinators = ctx.guild.get_role(717171411692683275)

        text = f"`{len(coordinators.members)}` Coordinators\n`{len(staff.members)}` Staff\n`{len(mentors.members)}` Mentors\n`{len(partners.members)}` \
            Partners\n`{len(bots.members)}` Bots\n`{len(attendees.members)}` Attendees\n`{len(everyone.members)}` All Members"
        embed = discord.Embed(
            title="ThetaHacks Stats", description=text, color=0x00ff9d)
        await ctx.send(embed=embed)

    @commands.command(name="ping")
    async def ping(self, ctx):
        start = time.perf_counter()
        message = await ctx.send("Ping...")
        end = time.perf_counter()
        duration = (end - start) * 1000
        await message.edit(content='Pong! {:.2f}ms'.format(duration))

    @commands.command(name="raffle")
    async def raffle(self, ctx):
        roleName = "Attendees"
        role = discord.utils.get(message.guild.roles, name=roleName)
        i = 0
        empty = True
        randomRaffle = 0
        randomRaffle = randrange(494)
        if role is None:
            await message.channel.send(f'There is no {roleName} role on this server!')
            return
            for member in message.guild.members:
                if role in member.roles:
                    i+=1
                    if (i == randomRaffle):
                        await message.channel.send("{0.name}".format(member))
                    else:
                        await message.channel.send(f"No User at {randomRaffle}")
                    empty = False
                    if empty:
                        await message.channel.send(f"Nobody has the role {roleName}".format(role.mention))


def setup(bot):
    print('commands')
    bot.add_cog(CommandsCog(bot))