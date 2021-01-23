# wow-za_bot.py
import os
import discord
from discord.ext import commands
import random
import re
from dotenv import load_dotenv
import tracemalloc

tracemalloc.start()
bot = commands.Bot(command_prefix = "&", description = "WoWzA Discord Bot")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot_user = bot.user

@bot.event
async def on_ready():
    """
    This event is called the bot is ready to accept payloads.
    This is called after login is successful.
    """
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "Hackers"))
#
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    ree_quotes = [
        '<a:wowzaree:784316745027551253>',
        '<a:wowzaree:784316745027551253> <a:wowzaree:784316745027551253>',
    ]

    wowza_bot_quotes = [
        '<a:wowzaree:784316745027551253>',
        'STAPH POKING ME',
        '<:REEEMaja:780569677461717063>',
        '<:REEE:568567509394128907>',
        '<:pepeREEEEEE:631257892313497610>',
        'WHAT DO YOU WANT?!',
        'STAPH BOTHERING ME I AM CLEARLY BUSY'
    ]

    if re.search("ree", message.content):
        response = random.choice(ree_quotes)
        await message.channel.send(response)

    if re.search("wowza", message.content, re.IGNORECASE) or re.search("bot", message.content, re.IGNORECASE):
        response = random.choice(wowza_bot_quotes)
        await message.channel.send(response)

    await bot.process_commands(message)

@bot.command()
async def querymsg(ctx, channel: discord.TextChannel = None, member: discord.Member = None):
    if channel and member:
        msg = discord.utils.get(await channel.history(limit=100).flatten(), author = member)
        await ctx.channel.send(msg)
    else:
        await ctx.channel.send("Please Supply Channel, and @username")
    # this gets the most recent message from a specified member in the past 100 messages
    # in a certain text channel - just an idea of how to use its

@bot.command()
async def print(ctx, arg):
    await ctx.channel.send(arg)
    await ctx.send("{} loaded.".format("user print initated"))

@bot.command()
async def create_vss_roster(ctx):
    await ctx.channel.send(
        """**__vSS__**
        *Raid description goes here, between two underscores.*
        ```ini
        [ SUN, JAN 1, 2021 | 2pm PST | +2 CST | +3 EST | +5 BST | +8 GMT ]```
        MT: @name
        Wearing: *set info*

        OT: @name
        Wearing: *set info*

        __**Head Stack:**__
        Group Healer: @name
        Wearing: *set info*

        DPS[*set info*][PL][T1]:
        DPS[*set info*][PM][T2]:
        DPS[*set info*][PR][T3]:
        DPS[*set info*]:

        __**Wing Stack:**__
        Cage Healer: @name
        Wearing: *set info*'"""
    )


if __name__ == "__main__":
    bot.run(TOKEN)
