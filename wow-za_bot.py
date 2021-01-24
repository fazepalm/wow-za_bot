# wow-za_bot.py
import os
import discord
from discord.ext import commands
import random
import re
from dotenv import load_dotenv
import tracemalloc
import json

##variables:
count_ree = 0
##
wowza_json_dict = {
    "count_ree" : count_ree
}
#

bot = commands.Bot(command_prefix = "&", description = "WoWzA Discord Bot")

tracemalloc.start()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    """
    This event is called the bot is ready to accept payloads.
    This is called after login is successful.
    """
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "Hackers"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    wowza_bot_quotes = [
        '<a:wowzaree:784316745027551253>',
        'STAPH POKING ME',
        '<:REEEMaja:780569677461717063>',
        '<:REEE:568567509394128907>',
        '<:pepeREEEEEE:631257892313497610>',
        'WHAT DO YOU WANT?!',
        'STAPH BOTHERING ME I AM CLEARLY BUSY'
    ]

    if re.search("^ree[e]+$|^ree$", message.content, re.IGNORECASE):
        global count_ree
        count_ree += 1
        ree_string = re.split("ree", message.content, flags=re.IGNORECASE)[-1]

        if re.search("ee", ree_string, re.IGNORECASE):
            ee_string_list = re.split("ee", ree_string, flags=re.IGNORECASE)
            ree_emote_list = ['<a:wowzaree:784316745027551253>']
            for count in range(1, (len (ee_string_list))):
                ree_emote_list.append('<a:wowzaree:784316745027551253>')
            response = " ".join(ree_emote_list)
        else:
            response = '<a:wowzaree:784316745027551253>'

        if (int(len(response)) >= 2000):
            await message.channel.send("Sorry You Have Hit Discord 2000 Char Limit, Try Again!")
        else:
            await message.channel.send(response)
        await message.channel.send("The Current Server 'REE' Count is: %d" % (int(count_ree)))

        wowza_json_dict["count_ree"] = count_ree
        ##create json writable:
        with open("wowza_bot_data.json", "w+") as write_file:
            json.dump(wowza_json_dict, write_file)
        write_file.close()

    if re.search("^wowza$|^wowza\s+", message.content, re.IGNORECASE) or re.search("^bot$|^bot\s+", message.content, re.IGNORECASE):
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
async def print_count_ree(ctx):
    await ctx.channel.send("The Current Server 'REE' Count is: %d" % (int(count_ree)))

#Trial pictures
@bot.command()
async def info_vmol(ctx):
    await ctx.channel.send(file=discord.File('trial_images/vmol_01.png'))
    await ctx.channel.send(file=discord.File('trial_images/vmol_02.gif'))
    await ctx.channel.send(file=discord.File('trial_images/vmol_03.png'))

@bot.command()
async def info_vas(ctx):
    await ctx.channel.send(file=discord.File('trial_images/vas_01.gif'))

@bot.command()
async def info_vcr(ctx):
    await ctx.channel.send(file=discord.File('trial_images/vcr_01.png'))
    await ctx.channel.send(file=discord.File('trial_images/vcr_02.png'))

@bot.command()
async def info_vss(ctx):
    await ctx.channel.send(file=discord.File('trial_images/vss_01.png'))
    await ctx.channel.send(file=discord.File('trial_images/vss_02.png'))

@bot.command()
async def info_vhof(ctx):
    await ctx.channel.send(file=discord.File('trial_images/vhof_01.png'))
    await ctx.channel.send(file=discord.File('trial_images/vhof_02.png'))
    await ctx.channel.send(file=discord.File('trial_images/vhof_03.png'))
    await ctx.channel.send(file=discord.File('trial_images/vhof_04.png'))

@bot.command()
async def info_vka(ctx):
    await ctx.channel.send("https://youtu.be/KEvc8niaNMk")

@bot.command()
async def info_vsg(ctx):
    await ctx.channel.send("https://www.youtube.com/watch?v=dnhcF6kROMc&start=980")
    await ctx.channel.send("https://www.youtube.com/watch?v=sUTwzKhAWSw")
    await ctx.channel.send("https://www.youtube.com/watch?v=0GsytONVaFw")
    await ctx.channel.send(file=discord.File('dungeon_images/vsg_01.png'))

@bot.command()
async def info_brp(ctx):
    await ctx.channel.send("https://www.heathen-horde.com/eso-guides/vet-blackrose-prison-unchained")
    await ctx.channel.send(
        """
Heathen Horde Vet Blackrose Prison UNCHAINED
GUIDE BY @HAKKU
This this the guide that I and my team (1 tank, 3 DPS) have been testing and figure out best suit our DPS and playstyle for our vBRP Unchained Tittle

Stage 1:
(Pay attention to the burn)

Round 1: Stack at Entrance then tank will pull all the adds in and cleave them together with the 2hand.

Round 2: Stack at Left side (from Entrance direction), kill 1 mage that will spawn then stack mid kill 1 wave of adds, then stack at entrance

Round 3: Stack Right, Kill mage, tank taunt 2hand on the left, then pull everything to the right side then clear adds.

Round 4: Wave stack entrance -> Clear adds then stack right, kill 1 wave of adds. Wave 2 will have a mage on left and right side, tanker will taunt everything on the Left and interrupt the left side mage, DPS stack on the Right -> kill mage then clear left side (Note: Make sure not to use any ultimate during this round to optimize the Balrogh buff)

Round 5: Boss fight -> switch gear to Balrogh then just burn the boss
        """
    )
    await ctx.channel.send(
        """
Stage 2:
(Note: Pay attention to crocodile and bugs small cone aoe, those are 1 shot mechanic, tank must pull spiders ASAP because the spiders hit really hard, they are highest pull priority for tank, Also recommend slot shield in this stage and purge to deal with shock shield reflection + poison bloom from those jellyfish. There will be also Hackwing that charge randomly from behind or from the flank direction, always be prepare to cast-blocking at all time because the amount of CC in this stage is insane)

Round 1: Stack at exit and just clear adds (Note: Don’t use destroy on first round)

Round 2: Save destro ultimate, kill adds on wave 1. On Wave 2 there will be a turtle (Forgot the name), drop all the destro ultimate to burn it -> clear adds.
        """
    )
    await ctx.channel.send(
        """
Round 3: Wave 3 will have 1 troll spawning at exit and another troll jumping from the left side, DPS must stack on the right side to avoid getting 1 shot from the jump and the stomp. Kill the first troll then tank will pull 2nd troll to the archer on the right side then cleave them down.

Round 4: There will be a Wamasu spawn at exit, cleave it together with adds. Then there will be 2 archers on left and right side, tank will taunt archer from right side then bring it to left side archer then cleave both of them (Note: Feel free to use ultimate in this round because we are taking it slow on last round)

Final: Slowly DPS the boss until around 70%, there will be a troll spawn -> kill it then slowly heavy attack the boss until around 64-62% -> there will be SWARM mechanic, all DPS stack together hold block on first tick, then heal + shield until SWARM gone. Then slowly burn the boss until Turtle spawn, then drop all destroy ultimate the burn the boss and Turtle together (Note: There will be 2 scenario in this case, Case 1: the boss and Turtle will stay together while DPS dropping destro ultimate and burn both of them together, then Wamasu will spawn immediately, tank must grab Wamasu. Case 2: If the boss teleport right after destro ultimate being dropped then just burn the Turtle then turn around slowly DPS and wait for 2nd SWARM, All DPS Stack together 1 more time then burn the boss, and ALWAYS ignore Wamasu).
        """
    )
    await ctx.channel.send(
        """
__**Stage 3: **__
Stack all mid. Nothing special in this stage, by far the easiest stage.

First 4 Round: Nothing special here, just pull all the adds in mid. There will be blood infuser, remember to bash them or they will enrage adds. DPS need to hold block + cast shield every new wave to avoid getting 1 shot. There will be garyole spawn every round, run to the side then run to mid to avoid Garoyle stomping AOE dropping in middle.

Final Round: Burn boss down to 60~50%, there will be first Colossus, then 2nd Colossus will spawn around 30%, after 2nd Colossus then burn the boss all the way till it die. (Note: Tank need to drop the BAT SWARM into corner, there will be the NOTIFIER. Also kill all the mages or they will summon extra Colossus.)
        """
    )
    await ctx.channel.send(
        """
Stage 4:
Round 1: Stack at exit kill 2hand on first wave. 2nd  wave will have 2 mages, Left & Right side, DPS will stack at left, kill the mage while tank will taunt and pull the right side mage to middle, then cleave them all down at mid. Then stack at exit to kill 2hand.

Round 2: Kill the mage that spawn on left side on 1st wave. On Wave 2 then burn down the SnB add because its CC is very frustrated and can lead to unnecessary death. There will be 2 archers, killing the archers will spawn the boss phase. There will be another 2 mages on left and right side, each DPS will taunt the mage on each side and run in opposite direction in order to pull them to Mid then cleave them together with the boss (Note: There will be some case where the mage will instantly case the AOE, each DPS will be in charge of interrupt of their opposite assigned mage. For example, if you taunt the left side mage, you will run to the right and interrupt the right side mage if it cast the AOE instead of running to Mid & vice versa)
        """
    )
    await ctx.channel.send(file=discord.File('arena_images/vbrp_01.png'))
    await ctx.channel.send(
        """
Round 3: nothing special here, stack at exit to kill the adds, a Turtle will spawn on left side, prefer a Magcro to drop Colossus to burn down the turtle, then the boss will spawn and DPS it down until it goes away at 64%.

Round 4: Stack mid, Tank need to pay attention to pull all the blood infuser, run to the side when garyole spawn then group at mid again, nothing special in this round.

Final: Slowly DPS Fire mage boss, then wait till 2nd boss spawn. Tank need to group 2 boss together to cleave them down. Wait till Wamasu spawn then drop all the ultimate, it will be enough to kill the first boss and Wamasu together, then tank will taunt the Turtle and run to the opposite direction. DPS down the 2nd boss and then kill the 3rd boss.
        """
    )
    await ctx.channel.send(
        """
Stage 5:

First 4 round: Nothing special here, but pay attention the AOE from all the adds because they hit really hard, there will be also an assigned DPS to kill totem. Prefer backbar vMA staff with Prismatic enchant to kill adds faster.

Final round: Burn the boss until the first Mechanic, assign each DPS on each lane (Mid, Left,Right) to pick up ghost (Note: Because the hitbox when picking up the ghost is really shitty, you have to sprint to make it easier to pick up ghost). Prefer someone run barrier on last stage in case if there are more than 2 ghosts weren’t picked up to avoid getting 1 shot. If missing 1 ghost, shield up then hold block. Tank will pull the boss to corner. Repeat the same process 2-3 times depend on DPS. Very easy stage.
        """
    )

#Trial roster creation
@bot.command()
async def create_vss_roster(ctx):
    await ctx.channel.send(
        """
**__vSS__**
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
Wearing: *set info*
        """
    )

#Trial CP INFO
@bot.command()
async def cp_vss(ctx):
    await ctx.channel.send(
    """
:dragon: __**CP for Sunspire**__ :dragon:
_The champion point allocations for veteran Sunspire. If it isn't listed here, it should be set to zero (0)._
    """
    )
    await ctx.channel.send(
    """
```diff
- TANK -
Ironclad ............. 81
---
Hardy ................ 43
Elemental Defender ... 49
Thick Skinned ........ 81
---
Heavy Armor Focus .... 16
```
```diff
+ HEALER +
Ironclad ............. 56
Spell Shield ......... 70
---
Elemental Defender ... 56
Thick Skinned ........ 56
---
Quick Recovery ....... 32
```
```ini
[ DPS ]
Ironclad ............. 56
Spell Shield ......... 70
---
Elemental Defender ... 56
Thick Skinned ........ 56
---
Quick Recovery ....... 32
```
```ini
[ Tombs DPS - HM only ]
Ironclad ............. 61
Spell Shield ......... 45
---
Elemental Defender ... 56
Thick Skinned ........ 44
---
Quick Recovery ....... 64
```
    """
    )

@bot.command()
async def cp_vcr(ctx):
    await ctx.channel.send(
    """
:eagle: __**CP for Cloudrest**__ :eagle:
_The champion point allocations for veteran Cloudrest. If it isn't listed here, it should be set to zero (0)._
```diff
- TANK -
Ironclad ............. 81
---
Hardy ................ 43
Elemental Defender ... 49
Thick Skinned ........ 81
---
Heavy Armor Focus .... 16
```
```diff
+ HEALER +
Ironclad ............. 56
Spell Shield ......... 70
---
Elemental Defender ... 56
Thick Skinned ........ 56
---
Quick Recovery ....... 32
```
```ini
[ DPS ]
Ironclad ............. 56
Spell Shield ......... 70
---
Elemental Defender ... 56
Thick Skinned ........ 56
---
Quick Recovery ....... 32
```
    """
    )

@bot.command()
async def cp_vhof(ctx):
    await ctx.channel.send(
    """
:robot: __**CP for Halls of Fabrication**__ :robot:
_The champion point allocations for veteran Halls of Fabrication. If it isn't listed here, it should be set to zero (0)._
```diff
- TANK -
Ironclad ............. 81
---
Hardy ................ 56
Elemental Defender ... 56
Thick Skinned ........ 66
---
Heavy Armor Focus .... 11
```
```diff
+ HEALER +
Ironclad ............. 72
---
Hardy ................ 56
Elemental Defender ... 56
Thick Skinned ........ 66
---
L/M Armor Focus ...... 20
```
```ini
[ DPS ]
Ironclad ............. 66
Spell Shield ......... 33
---
Hardy ................ 56
Elemental Defender ... 56
Thick Skinned ........ 48
---
Quick Recovery ....... 11
```
    """
    )

if __name__ == "__main__":
    bot.run(TOKEN)
