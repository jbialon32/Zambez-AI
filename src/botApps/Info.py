'''
Created on Jan 17, 2018

Made for Zambez-AI

@author: Kalerne aka dBasshunterb
'''

import discord

def Info(bot):
    @bot.command(pass_context=True)    
    async def info(ctx, user: discord.Member):
            await bot.say("The users name is: {}\n".format(user.name) +
                         "The users ID is: {}\n".format(user.id) +
                         "The users status is: {}\n".format(user.status) +
                         "The users highest roll is: {}\n".format(user.top_role) +
                         "The user joined at: {}".format(user.joined_at))