import rpg_utils
from discord.ext import commands

bot = commands.Bot(command_prefix = '.rpg ')

@bot.command()
async def begin(ctx):
    if rpg_utils.playerexists(ctx.author):

        await ctx.send("You've already begun your journey!")
    else:

        rpg_utils.addplayer(ctx.author)

        await ctx.send("And so it begins...\nUse `.rpg class <1-" + str(len(rpg_utils.classes)) + ">` to select a player class from the following list:\n`" + ", ".join(rpg_utils.classes) + "`")


@bot.command(name = 'class')
async def _class(ctx, number):

    player = rpg_utils.getplayer(ctx.author)

    if player._can_change_class:

        if number.isDigit() and int(number) < len(rpg_utils.classes) and int(number) >= 1:

            player._can_change_class = False

            player._class = rpg_utils.classes[int(number)+1]

            ctx.send("Successfully set your class to **" + player._class + ".**")
        else:

            ctx.send("Invalid arguments! Try providing a number, 1-"+str(len(rpg_utils.classes))+".")
    else:

        ctx.send("You can't change your class right now.\nCurrent class: " + player._class)

token = ""

with open("token.cfg") as f:
    token = f.readlines()[0]
    
bot.run(token)

