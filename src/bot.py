'''
Created on Jan 15, 2018

Made for Zambez-AI

@author: Kalerne aka dBasshunterb
'''

from discord.ext import commands
from botApps.Info import Info
from botApps.MonsterFinder import Monster
from botApps.SpellFinder import SpellFinder
from botApps.Dice import Dice
from botApps.Thanks import Thanks

file = open("text.txt" , 'r')
text = file.readline()
file.close

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print('#Zambiez-AI initiated\n' +
          '# is my call.\n' +
          '#commandlist in discord for readme.\n' +
          '#Coded by Kalerne aka dBasshunterb')
    
@bot.command(pass_context=True)
async def commandlist(ctx):
    await bot.say("info [insert username]: Gives users basic information\n" +
                  "dice [number of sides (default=6 min=2 max=9999)] [number of die(default=1 max=4)]: Rolls dice and totals result\n" +
                  "monster [Name(use '_' in place of space)]: Returns DnD Monster info\n" +
                  "spell [Name(use '_' in place of space)]: Returns DnD Spell info\n" +
                  "thanks: Gives thanks for my work :)")
    
Info(bot)
Dice(bot)        
Monster(bot)
SpellFinder(bot)
Thanks(bot)
    
bot.run(text)