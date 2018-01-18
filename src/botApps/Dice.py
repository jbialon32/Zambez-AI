'''
Created on Jan 17, 2018

Made for Zambez-AI

@author: Kalerne aka dBasshunterb
'''
from random import randint
from builtins import sum

def Dice(bot):
    @bot.command(pass_context=True)
    async def dice(ctx, numSides=6, numDice=1):
    
        numDice = int(numDice)
        
        if numDice > 4:
            await bot.say("Please keep number of dice under 6")
            return
        
        if numDice < 1:
            await bot.say("Must roll at least 1 die")
            return
        
        if numSides > 9999:
            await bot.say("Keep number of sides under 10,000")
            return
        
        if numSides < 2:
            await bot.say("Die must have at least 2 sides")
            return
        
        try:
            rolls = []
        
            while numDice > 0:
                d20 = randint(1, numSides)
                rolls.append(d20)
                numDice -= 1
        
            rolls.sort(reverse=True)
            totalRoll = sum(rolls)
                
            for roll in rolls:
                numDice += 1
                await bot.say("Die #{} lands on {}".format(numDice, roll))
            
            await bot.say("The total roll is {}".format(totalRoll))
            return totalRoll
        
        except:
            await bot.say("Please use the correct syntax")
            await bot.say('"#dice (INTEGER NUMBER) (INTEGER NUMBER"')