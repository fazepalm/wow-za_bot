# wow-za_bot.py
import os
import discord
from discord.ext import commands
import random
import re
from dotenv import load_dotenv

bot = commands.Bot(command_prefix = "&")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    # Setting `Watching ` status
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "Hackers"))
    print(f'{bot.user} has connected to Discord!')

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

@bot.command()
async def querymsg(ctx, channel: discord.TextChannel, member: discord.Member):
    msg = discord.utils.get(await channel.history(limit=100).flatten(), author = member)
    await ctx.channel.send(msg)
    # this gets the most recent message from a specified member in the past 100 messages
    # in a certain text channel - just an idea of how to use its versatility

@bot.command()
async def print(ctx, arg):
    await ctx.channel.send(arg)

bot.run(TOKEN)
