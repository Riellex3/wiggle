# bot.py
import os
import random
import pathlib
import time
import datetime
import asyncio
from itertools import cycle
import json

import math
from datetime import date
import discord
from discord import channel
from discord.ext import commands, tasks
from dotenv import load_dotenv
from PIL import Image, ImageSequence, ImageDraw, ImageFont
from io import BytesIO

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
wiggleGuild_id=502816815446097920
wigglebotChannel_id=503826113370390528
eventreminderrole_id=878768826890727434
votereminderrole_id=880623438597877760

# Enables intents for bot to detect members list
# intents = discord.Intents.default()
# intents.members = True
# client = discord.Client(intents=intents)

#initialize bot
bot = commands.Bot(command_prefix='~', case_insensitive=True)
print('Running...')

dir_path = os.path.dirname(os.path.realpath(__file__))
dasheventreminder=['01:55','05:55','09:55','13:55','17:55','21:55']
dasheventtimes=['02:00','06:00','10:00','14:00','18:00','22:00']
gauntleteventreminder=['00:55','02:55','04:55','06:55','08:55','10:55','12:55','14:55','16:55','18:55','20:55','22:55']
pierreeventreminder=['03:55','07:55','11:55','15:55','19:55','23:55']
pierreeventtimes=['00:00','04:00','08:00','12:00','16:00','20:00']
gauntleteventtimes=['01:00','03:00','05:00','07:00','09:00','11:00','13:00','15:00','17:00','19:00','21:00','23:00']
alleventtimes = ['02:00','06:00','10:00','14:00','18:00','22:00']
# alleventtimes= ['00:00','01:00','03:00','04:00','05:00','07:00','08:00','09:00','11:00','12:00','13:00','15:00','16:00','17:00','19:00','20:00','21:00','23:00']
voteremindertimes=['12:00','23:00']
# testeventreminder=['08:37']

bosstimerList=[[-1 for j in range(20)] for i in range(42)]
bossList = [['mano',3],['stumpy',3],['deo',3],['king_clang',3],['seruf',3],['faust',3],['giant_centipede',3],['timer',3],['mushmom',3],['dyle',3],['zombie_mushmom',3],['zeno',3],['nine-tailed_fox',3],['tae_roon',3],['king_sage_cat',3],['jrbalrog',3],['eliza',3],['snack_bar',3],['chimera',3],['blue_mushmom',23],['snowman',3],['headless_horseman',6],['manon',3],['griffey',3],['pianus_left',24],['pianus_right',16],['bigfoot',12],['black_crow',23],['leviathan',2],['kacchuu_musha',11],['dodo',3],['anego',5],['lilynouch',3],['lyka',3],['bftp1',12],['bftp2',12],['bftp3',12],['bftp4',12],['bftp5',12],['bffp',12],['bfed',12],['bfer',12]]

@tasks.loop(seconds = 1)
async def remindevent():
    serverTime=time.gmtime()
    botchanno = bot.get_channel(wigglebotChannel_id)
    botguild = bot.get_guild(wiggleGuild_id)
    eventreminderrole = botguild.get_role(eventreminderrole_id)
    votereminderrole = botguild.get_role(votereminderrole_id)
    # testreminderrole = botguild.get_role(879644343563079760)
    # await botchanno.send(f'The current time is: {time.strftime("%H:%M", serverTime)}\nThe next event is at {testeventreminder[0]}')
    # if time.strftime("%H:%M",serverTime) in gauntleteventreminder:
    #     print(f'{time.strftime("%H:%M", serverTime)} the Halloween Gauntlet will begin in 5 minutes!')
    #     await botchanno.send(f'{eventreminderrole.mention} the Halloween Gauntlet will begin in 5 minutes!')
    #     await asyncio.sleep(70)
    # if time.strftime("%H:%M",serverTime) in pierreeventreminder:
    #     print(f'{time.strftime("%H:%M", serverTime)} Pierre will spawn in 5 minutes!')
    #     await botchanno.send(f'{eventreminderrole.mention} Pierre will spawn in 5 minutes!')
    #     await asyncio.sleep(70)
    if time.strftime("%H:%M",serverTime) in dasheventreminder:
        print(f'{time.strftime("%H:%M", serverTime)} Winter Dash is in 5 minutes!')
        await botchanno.send(f'{eventreminderrole.mention} Winder Dash is in 5 minutes!')
        await asyncio.sleep(70)
    if time.strftime("%H:%M",serverTime) in voteremindertimes:
        print(f'{time.strftime("%H:%M",serverTime)} don''t forget to vote!')
        await botchanno.send(f'{votereminderrole.mention} don''t forget to vote!')
        await asyncio.sleep(70)
    # if time.strftime("%H:%M",serverTime) in testeventreminder:
    #     print(f'{time.strftime("%H:%M",serverTime)} test')
    #     await botchanno.send(f'{testreminderrole.mention} uwu')
    #     await asyncio.sleep(70)
    await asyncio.sleep(2)

#################################################################################### Discord Features
# Author
@bot.command(name='author', help='About the author')
async def author(ctx):
    await ctx.send('Author: Rielle (Riellex3)')
    await ctx.send('Thank you for using my bot! Please feel free to reach out to me if you have any questions/suggestions for improvement!')
    await ctx.send(file=discord.File(dir_path+'/rie.png'))

@bot.event
async def on_ready():
    remindevent.start()
    print('Bot is ready.')
    await bot.change_presence(activity=discord.Game(name='WapleRoyals'))

# React to its own message
@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user or user.bot:
        return
    channel = reaction.message.channel
    # await channel.send(f'{user}, reacted with {reaction.emoji}')
    # if reaction.message.author == bot.user:
    #     await reaction.message.edit(content = f'{reaction.emoji}')
    #     await reaction.message.clear_reaction(reaction.emoji)
    # Boss timer
    try:
        embeds = reaction.message.embeds
    except IndexError:
        return

    # Boss Timer Change Page
    if 'Here are the timers for area bosses' in embeds[0].description:
        if reaction.emoji == '⬅':
            embed1=discord.Embed()
            embed1.description = 'Here are the timers for area bosses\n\n**Mano:** 3 Hours\n**Stumpy:** 3 Hours\n**Deo:** 3 Hours\n**King Clang:** 3 Hours\n**Seruf:** 3 Hours\n**Faust:** 3 Hours\n**Giant Centipede:** 3 Hours\n**Timer:** 3 Hours\n**Mushmom:** 3 Hours\n**Dyle:** 3 Hours\n**Zombie Mushmom:** 3 Hours\n**Zeno:** 3 Hours\n**Nine-Tailed Fox:** 3 Hours\n**Tae Roon:** 3 Hours\n**King Sage Cat:** 3 Hours\n**Jr. Balrog:** 3 Hours\n**Eliza:** 3 Hours\n\nPage 1 of 2'
            await reaction.message.clear_reaction('⬅')
            await reaction.message.clear_reaction('➡')
            await reaction.message.add_reaction('➡')
            await reaction.message.edit(embed=embed1)
            
        if reaction.emoji == '➡':
            embed2 = discord.Embed()
            embed2.description = 'Here are the timers for area bosses\n\n**Snack Bar:** 3 Hours\n**Chimera:** 3 Hours\n**Blue Mushmom:** 23 Hours\n**Snowman:** 3 Hours\n**Headless Horseman:** 6 Hours\n**Manon:** 3 Hours\n**Griffey:** 3 Hours\n**Pianus(Left):** 24 Hours\n**Pianus(Right):** 16 Hours\n**Bigfoot:** 12 Hours\n**Black Crow:** 23 Hours\n**Leviathan:** 2 Hours\n**Kacchuu Musha:** 11 Hours\n**Dodo:** 3 Hours\n**Anego:** 5 Hours\n**Lilynouch:** 3 Hours\n**Lyka:** 3 Hours\n\nPage 2 of 2'
            await reaction.message.clear_reaction('⬅')
            await reaction.message.clear_reaction('➡')
            await reaction.message.add_reaction('⬅')
            await reaction.message.edit(embed=embed2)

# Repeat message back to user
@bot.command(name = 'repeat', help = 'Repeats the message back to the user')
async def repeat(ctx, *, message):
    repeatMessage = ''
    index = 0
    for char in message:
        if index % 2 == 1:
            repeatMessage += char.upper()
        else:
            repeatMessage += char
        index += 1
        if char == ' ':
            index += 1
    await ctx.send(f'{repeatMessage}')


# Display Area Boss Timers
@bot.command(name='bosstimer', help = 'Displays Area Boss Timers')
async def bosstimer(ctx):
    
    embed1 = discord.Embed()
    embed1.description = 'Here are the timers for area bosses\n\n**Mano:** 3 Hours\n**Stumpy:** 3 Hours\n**Deo:** 3 Hours\n**King Clang:** 3 Hours\n**Seruf:** 3 Hours\n**Faust:** 3 Hours\n**Giant Centipede:** 3 Hours\n**Timer:** 3 Hours\n**Mushmom:** 3 Hours\n**Dyle:** 3 Hours\n**Zombie Mushmom:** 3 Hours\n**Zeno:** 3 Hours\n**Nine-Tailed Fox:** 3 Hours\n**Tae Roon:** 3 Hours\n**King Sage Cat:** 3 Hours\n**Jr. Balrog:** 3 Hours\n**Eliza:** 3 Hours\n\nPage 1 of 2'

    m = await ctx.send(embed=embed1)
    await m.add_reaction('➡')

# Wiggle
@bot.command(name='wiggle', help='Wiggle your butt!')
async def wiggle(ctx):
    await ctx.send(file=discord.File(dir_path+'/wiggle'+str(random.randint(1,18))+'.gif'))

# Keyboard
@bot.command(name='keyboard', help='Eat Keyboard')
async def keyboard(ctx):
    await ctx.send(file=discord.File(dir_path+'/keyboard'+str(random.randint(1,8))+'.gif'))

# Keep Eat
@bot.command(name='keepeat', help='Keep eat')
async def keepeat(ctx):
    await ctx.send(file=discord.File(dir_path+'/keepeat.gif'))

# Mine Idol
@bot.command(name='idol', help='Mine idol')
async def idol(ctx):
    await ctx.send(file=discord.File(dir_path+'/mineidol.gif'))

@bot.command(name = 'splats', help = 'Splats the user')
async def splats(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    goggles = Image.open('goggles.png')
    #goggles = goggles.resize(83, 130)
    lips = Image.open('lips.png')

    asset = user.avatar_url_as(format='png', size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp.thumbnail((128,128), Image.ANTIALIAS)

    goggles.convert('RGBA')
    pfp.paste(goggles, (20,20), goggles)
    pfp.paste(lips, (25,60), lips)
    pfp.save('profile.png')


    await ctx.send(file = discord.File("profile.png"))

@bot.command(name = 'feed', help = 'Feed the user')
async def feed(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    keyboard = Image.open('eatkeyboard.gif')

    asset = user.avatar_url_as(format='png', size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp.thumbnail((128,128), Image.ANTIALIAS)

    frames = []
    for frame in ImageSequence.Iterator(keyboard):
        frame = frame.copy()
        frame=frame.convert('RGBA')
        pfp.paste(frame, (20,60), frame)
        pfp.save('profile.png')
        frames.append(pfp)
        pfp = Image.open(data)
        pfp.thumbnail((128,128), Image.ANTIALIAS)
    frames[0].save('profile.gif', save_all=True, append_images=frames[1:], duration=500, loop=0)
    await ctx.send(file = discord.File("profile.gif"))

@bot.command(name = 'pat', help = 'Pat the user')
async def feed(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    pat = Image.open('pat.gif')
    asset = user.avatar_url_as(format='png', size = 256)
    data = BytesIO(await asset.read())

    pfp = Image.open(data)
    pfp.thumbnail((128,128), Image.ANTIALIAS)
    pfp.save('pfp.png')
    pfp = Image.open('pfp.png')
    pfp = pfp.resize((256,256), Image.ANTIALIAS)

    count = 0
    posx = 180
    posy = 180
    imx = 256
    imy = 256
    frames = []
    for frame in ImageSequence.Iterator(pat):
        frame = frame.copy()
        frame=frame.convert('RGBA')
        blankuse = Image.open('cloudstock.png')
        blankuse.paste(pfp, (posx,posy))
        blankuse.paste(frame, (0,0), frame)
        
        frames.append(blankuse)
        count = count+1
        if count == 1:
            imx = imx + 40
            posx = posx - 20
            imy = imy - 20
            posy = posy + 20
        if count == 3:
            imx = imx + 30
            posx = posx - 15
            imy = imy - 30
            posy = posy + 30
        if count == 5:
            imx = imx - 10
            posx = posx + 5
            imy = imy + 20
            posy = posy - 20
        if count == 6:
            imx = imx - 20
            posx = posx + 10
            imy = imy + 20
            posy = posy - 20
        pfp = pfp.resize((imx,imy), Image.ANTIALIAS)
        # blankuse = Image.alpha_composite(blankuse, frame)
        # pfp.thumbnail((128,128), Image.ANTIALIAS)
    frames[0].save('profile.gif', save_all=True, append_images=frames[1:], duration=50, loop=0)
    await ctx.send(file = discord.File("profile.gif"))

@bot.command(name = 'floor', help = 'The floor is...')
async def slap(ctx, user:discord.Member = None, *args):
    text = ''
    for arg in list(args):
        text = text + arg + ' '
    
    slap = Image.open('floor.jpg')
    
    asset = user.avatar_url_as(format = 'jpg', size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp.thumbnail((32,32), Image.ANTIALIAS)
    pfp = pfp.convert('RGBA')

    slap.paste(pfp, (100,100))
    slap.paste(pfp, (330,85))
    draw = ImageDraw.Draw(slap)
    font = ImageFont.truetype("COMIC.TTF", size = 26)
    draw.text((170,30),text, fill = (0,0,0), font=font)
    slap.save('profile.png')
    await ctx.send(file = discord.File('profile.png'))

@bot.command(name = 'slap', help = 'Slap!')
async def slap(ctx, user:discord.Member = None):
    if user == None:
        user = ctx.author
    if user.name == 'potatosticks':
        await ctx.send('You can''t slap the queen!')
        return
    
    slap = Image.open('slap.gif')
    

    asset = user.avatar_url_as(format = 'jpg', size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp.thumbnail((128,128), Image.ANTIALIAS)
    pfp = pfp.convert('RGBA')


    frames = [f.copy() for f in ImageSequence.Iterator(slap)]
    for i, frame in enumerate(frames):
        frame = frame.convert("RGBA")
        if i < 21:
            frame.paste(pfp, (310, 95))
        elif i < 27:
            pfp.thumbnail((64,64), Image.ANTIALIAS)
            frame.paste(pfp, (300, 50))
        elif i < 30:
            pfp.thumbnail((64,64), Image.ANTIALIAS)
            frame.paste(pfp, (290, 40))
        elif i < 31:
            pfp.thumbnail((64,64), Image.ANTIALIAS)
            frame.paste(pfp, (300, 50))
        elif i < 33:
            pfp.thumbnail((64,64), Image.ANTIALIAS)
            frame.paste(pfp, (300, 50))    
        elif i < 35:
            pfp.thumbnail((64,64), Image.ANTIALIAS)
            frame.paste(pfp, (350, 60))   
        else:
            pfp.thumbnail((64,64), Image.ANTIALIAS)
            frame.paste(pfp, (350, 65))
        
        frames[i] = frame
    
    frames[0].save('profile.gif', save_all=True, append_images=frames[1:], duration=40, loop=0)
    await ctx.send(file = discord.File('profile.gif'))

@bot.command(name = 'dummy', help = 'Simulates a series of dummy scrolls')
async def dummy(ctx, scrolls: int):
    passes = 0
    fails = 0
    attempts = ''
    rate = ''
    counter = 0
    # if scrolls:
    for i in range(scrolls):
        pf = round(random.random(),2)
        if pf < 0.10:
            passes = passes + 1
            attempts = attempts + str(i) + '   '
            rate = rate + str(passes) + '/' + str(counter) + '   '
            counter = 0
        else:
            fails = fails + 1
        counter = counter + 1


    if passes > 1:
        await ctx.send(file = discord.File('scrollpassed.gif'))
        await ctx.send(f'You have passed {passes} out of {scrolls} dummies.\nYou passed on attempts:    {attempts}\nYour rates are: {rate}')
        return
    await ctx.send(file = discord.File('scrollfailed.gif'))
    await ctx.send(f'You have failed all your dummies')



@bot.command(name = 'cs', help = 'Simulates a chaos scroll')
async def cs(ctx, *argv: int):
    P5 = 0.99
    P4 = 1.98
    P3 = 10.21
    P2 = 15.87
    P1 = 19.31
    P0 = 18.38
    P_1 = 13.70
    P_2 = 8.00
    P_3 = 3.65
    P_4 = 2.97
    P_5 = 4.94

    R5 = P5
    R4 = R5 + P4
    R3 = R4 + P3
    R2 = R3 + P2
    R1 = R2 + P1
    R0 = R1 + P0
    R_1 = R0 + P_1
    R_2 = R_1 + P_2
    R_3 = R_2 + P_3
    R_4 = R_3 + P_4
    R_5 = R_4 + P_5
    stats = ''
    cses = ''
    
    if not argv:
        rng = round(random.random()*100,2)
        cs = random.choice([-5,-4,-3,-2,-1,0,1,2,3,4,5])
        cses = str(cs)
    
    for arg in argv:
        rng = round(random.random()*100,2)
        cs = random.choice([-5,-4,-3,-2,-1,0,1,2,3,4,5])
        cses = cses + str(cs) + ' '
        if arg == 0:
            result = arg
            stats = stats + str(result) + '\n'
            continue
        result = arg+cs
        if result < 0:
            result = 0
        stats = stats + str(result) + '\n'
    
    pf = round(random.random(),2)
    print(pf)
    if pf > 0.6:
        await ctx.send(file = discord.File('scrollfailed.gif'))
        return
    await ctx.send(file = discord.File('scrollpassed.gif'))
    await asyncio.sleep(2)
    if argv:
        await ctx.send(f'Your cs boosted your stats by {cses}\nYour new stats are\n{stats}')
    else:
        await ctx.send(f'Your cs boosted your stats by {cses}')

@bot.command(name = 'csp', help = 'Simulates a successful chaos scroll')
async def csp(ctx, *argv: int):
    P5 = 0.99
    P4 = 1.98
    P3 = 10.21
    P2 = 15.87
    P1 = 19.31
    P0 = 18.38
    P_1 = 13.70
    P_2 = 8.00
    P_3 = 3.65
    P_4 = 2.97
    P_5 = 4.94

    R5 = P5
    R4 = R5 + P4
    R3 = R4 + P3
    R2 = R3 + P2
    R1 = R2 + P1
    R0 = R1 + P0
    R_1 = R0 + P_1
    R_2 = R_1 + P_2
    R_3 = R_2 + P_3
    R_4 = R_3 + P_4
    R_5 = R_4 + P_5
    stats = ''
    cses = ''
    
    if not argv:
        rng = round(random.random()*100,2)
        cs = random.choice([-5,-4,-3,-2,-1,0,1,2,3,4,5])
        cses = str(cs)
    
    for arg in argv:
        rng = round(random.random()*100,2)
        cs = random.choice([-5,-4,-3,-2,-1,0,1,2,3,4,5])
        cses = cses + str(cs) + ' '
        result = arg+cs
        if arg == 0:
            result = arg
            stats = stats + str(result) + '\n'
            continue
        if result < 0:
            result = 0
        stats = stats + str(result) + '\n'
    
    await ctx.send(file = discord.File('scrollpassed.gif'))
    await asyncio.sleep(2)
    if argv:
        await ctx.send(f'Your cs boosted your stats by {cses}\nYour new stats are\n{stats}')
    else:
        await ctx.send(f'Your cs boosted your stats by {cses}')


# @bot.command(name = 'boba', help = 'Boba')
# async def boba(ctx, user:discord.Member = None):
#     if user == None:
#         user = ctx.author
    
#     bobacat = Image.open('bobacat.gif')
    

#     asset = user.avatar_url_as(format = 'jpg', size = 128)
#     data = BytesIO(await asset.read())
#     pfp = Image.open(data)
#     pfp.thumbnail((128,128), Image.ANTIALIAS)
#     pfp = pfp.convert('RGBA')
    

#     frames = [f.copy() for f in ImageSequence.Iterator(bobacat)]
#     for i, frame in enumerate(frames):
#         frame = frame.convert("RGBA")
#         # if i < 21:
#         #     frame.paste(pfp, (310, 95))
#         # elif i < 27:
#         #     pfp.thumbnail((64,64), Image.ANTIALIAS)
#         #     frame.paste(pfp, (300, 50))
#         # elif i < 30:
#         #     pfp.thumbnail((64,64), Image.ANTIALIAS)
#         #     frame.paste(pfp, (290, 40))
#         # elif i < 31:
#         #     pfp.thumbnail((64,64), Image.ANTIALIAS)
#         #     frame.paste(pfp, (300, 50))
#         # elif i < 33:
#         #     pfp.thumbnail((64,64), Image.ANTIALIAS)
#         #     frame.paste(pfp, (300, 50))    
#         # elif i < 35:
#         #     pfp.thumbnail((64,64), Image.ANTIALIAS)
#         #     frame.paste(pfp, (350, 60))   
#         # else:
#         #     pfp.thumbnail((64,64), Image.ANTIALIAS)
#         #     frame.paste(pfp, (350, 65))
#         frame.paste(pfp, (200,200), pfp)
#         frames[i] = frame
    
#     frames[0].save('profile.gif', save_all=True, append_images=frames[1:], duration=40, loop=0)
#     await ctx.send(file = discord.File('profile.gif'))

# assigns eventreminder role to user
@bot.command(name='eventreminder', help = 'Assigns the eventremminder role to the user to be reminded of scheduled events')
async def eventreminder(ctx):
    member = ctx.message.author
    role = discord.utils.get(member.guild.roles, name = 'eventreminder')
    if role in member.roles:
        await member.remove_roles(role)
        await ctx.send('You have been removed from the eventreminder role')
        return
    await member.add_roles(role)
    await ctx.send('You have been added the eventreminder role to be alerted for upcoming events.')

# assigns voetreminder role to user
@bot.command(name='votereminder', help = 'Assigns the votereminder role to the user to be reminded to vote every 12 hours')
async def votereminder(ctx):
    member = ctx.message.author
    role = discord.utils.get(member.guild.roles, name = 'votereminder')
    if role in member.roles:
        await member.remove_roles(role)
        await ctx.send('You have been removed from the votereminder role')
        return
    await member.add_roles(role)
    await ctx.send('You have been added the votereminder role to be reminded to vote.')

# Get servertime
@bot.command(name = 'servertime', help = 'States the current servertime')
async def servertime(ctx):
    serverTime=time.gmtime()
    await ctx.send(f'The current time is: {time.strftime("%H:%M:%S", serverTime)}')
#region Boss Timer
# # Sets a timer for a certain boss
# @bot.command(aliases = ['bt'], help = "Sets a timer for a certain boss, given the boss and channel. Note that all area bosses have randomized timers between -20% and +20% of their respawn time\n Options for bosses are: ['mano','stumpy','deo','king_clang','seruf','faust','giant_centipede','timer','mushmom','dyle','zombie_mushmom','zeno','nine-tailed_fox','tae_roon','king_sage_cat','jrbalrog','eliza', 'snack_bar','chimera','blue_mushmom','snowman','headless_horseman','manon','griffey','pianus_left','pianus_right','bigfoot','black_crow','leviathan','kacchuu_musha','dodo','anego','lilynouch','lyka','bftp1','bftp2','bftp3','bftp4','bftp5','bffp','bfed','bfer']")
# async def bosstime(ctx, boss: str, chan: int):
#     # embed1.description = 'Here are the timers for area bosses\n\n**Mano:** 3 Hours\n**Stumpy:** 3 Hours\n**Deo:** 3 Hours\n**King Clang:** 3 Hours\n**Seruf:** 3 Hours\n**Faust:** 3 Hours\n**Giant Centipede:** 3 Hours\n**Timer:** 3 Hours\n**Mushmom:** 3 Hours\n**Dyle:** 3 Hours\n**Zombie Mushmom:** 3 Hours\n**Zero:** 3 Hours\n**Nine-Tailed Fox:** 3 Hours\n**Tae Roon:** 3 Hours\n**King Sage Cat:** 3 Hours\n**Jr. Balrog:** 3 Hours\n**Eliza:** 3 Hours\n\nPage 1 of 2'
#     # embed2.description = 'Here are the timers for area bosses\n\n**Snack Bar:** 3 Hours\n**Chimera:** 3 Hours\n**Blue Mushmom:** 23 Hours\n**Snowman:** 3 Hours\n**Headless Horseman:** 6 Hours\n**Manon:** 3 Hours\n**Griffey:** 3 Hours\n**Pianus(Left):** 24 Hours\n**Pianus(Right):** 16 Hours\n**Bigfoot:** 12 Hours\n**Black Crow:** 23 Hours\n**Leviathan:** 2 Hours\n**Kacchuu Musha:** 11 Hours\n**Dodo:** 3 Hours\n**Anego:** 5 Hours\n**Lilynouch:** 3 Hours\n**Lyka:** 3 Hours\n\nPage 2 of 2'
#     # Define the timer (in hours) depending on what the boss is
#     # bossList = ['mano','stumpy','deo','king_clang','seruf','faust','giant_centipede','timer','mushmom','dyle','zombie_mushmom','zeno','nine-tailed_fox','tae_roon','king_sage_cat','jrbalrog','eliza', 'snack_bar','chimera','blue_mushmom','snowman','headless_horseman','manon','griffey','pianus_left','pianus_right','bigfoot','black_crow','leviathan','kacchuu_musha','dodo','anego','lilynouch','lyka']

#     for j in range(len(bossList)):
#         if bossList[j][0] == boss:
#             index = j
#             break
#     # Convert to hours
#     try:
#         timer = bossList[index][1]*60*60
#     except UnboundLocalError:
#         await ctx.send('Please enter a valid boss')
#         return
#     highBound = int(timer*1.2)

#     if bosstimerList[index][chan-1] != -1:
#         await ctx.send(f'{boss.title()} Ch{chan} timer has been cleared.')
#         bosstimerList[index][chan-1] = 'stop'
#         return

#     try:
#         bosstimerList[index][chan-1] = timer
#     except IndexError:
#         await ctx.send('Please enter a valid channel')
#         return
#     await ctx.send(f'{boss.title()} in channel {chan} will respawn in approximately {int(timer/3600)} hours.')
#     for i in range(highBound):
#         if bosstimerList[index][chan-1] != 'stop':
#             bosstimerList[index][chan-1] -= 1
#         else:
#             bosstimerList[index][chan-1] = -1
#             return
#         await asyncio.sleep(1)
#     bosstimerList[index][chan-1] = -1
#     await ctx.send(f'{boss.title()} in channel {chan} has respawned!')
    
    
# @bot.command(name = 'checkboss', help = 'Checks if a boss has respawned')
# async def checkboss(ctx, boss) :
#     string = ''
#     for j in range(len(bossList)):
#         if boss in bossList[j][0]:
#             index = j
#             for i in range(0,20):
#                 if bosstimerList[index][i] != -1:
#                     bossValueHour = bossList[index][1]*3600
#                     lowSecondsLeft = int(0.8*bossValueHour-bossValueHour+bosstimerList[index][i])
#                     lowHoursLeft = int(lowSecondsLeft/3600)
#                     lowSecondsLeft = lowSecondsLeft-lowHoursLeft*3600
#                     lowMinutesLeft = int(lowSecondsLeft/60)
#                     lowSecondsLeft = lowSecondsLeft-lowMinutesLeft*60

#                     highSecondsLeft = int(1.2*bossValueHour-bossValueHour+bosstimerList[index][i])
#                     highHoursLeft = int(highSecondsLeft/3600)
#                     highSecondsLeft = highSecondsLeft-highHoursLeft*3600
#                     highMinutesLeft = int(highSecondsLeft/60)
#                     highSecondsLeft = highSecondsLeft-highMinutesLeft*60
#                     if lowHoursLeft <= 0 or lowMinutesLeft <= 0 or lowSecondsLeft <= 0:
#                         string += (f'{bossList[index][0].title()} in channel {i+1} will spawn anytime between now and {highHoursLeft}h{highMinutesLeft}m{highSecondsLeft}s\n')
#                     else:
#                         string += (f'{bossList[index][0].title()} in channel {i+1} will spawn in anytime between {lowHoursLeft}h{lowMinutesLeft}m{lowSecondsLeft}s and {highHoursLeft}h{highMinutesLeft}m{highSecondsLeft}s\n')
#     if string == '':
#         string += (f'There are no channels logged for {boss}')
#     await ctx.send(string)
#endregion Bosstimer

# Get time until next event
@bot.command(name='nextevent', help = 'States the time until next event')
async def nextevent(ctx):
    # Get current time
    serverTime = time.gmtime()
    # Pull Hours and Minutes from current servertime
    sHour = int(time.strftime("%H", serverTime))
    sMinute = int(time.strftime("%M", serverTime))
    eventName = ''
    # Checks if there are events
    try:
        alleventtimes[0]
    except (TypeError, ValueError, IndexError):
        await ctx.send('There are no upcoming events')
        return

    for str in alleventtimes:
        eHour = int(str[0:2])
        eMinute = int(str[3:5])
        hoursUntil = eHour-sHour
        minutesUntil = eMinute-sMinute
        # For analyzing purposes
        # print(f'eHour = {eHour}')
        # print(f'sHour = {sHour}')
        # print(f'eMinute = {eMinute}')
        # print(f'sMinute = {sMinute}')
        # print(str)
        # print(f'hoursUntil = {hoursUntil}')
        if hoursUntil > 0:
            if minutesUntil >= 0:
                # print('Pass1')
                # if str in pierreeventtimes:
                    # eventName = 'Pierre'
                # elif str in gauntleteventtimes:
                #     eventName = 'Halloween Gauntlet'
                if str in dasheventtimes:
                    eventName = 'Winter Dash'
                await ctx.send(f'{eventName} is in {hoursUntil} hour(s) and {minutesUntil} minute(s) at {str}')
                return
            if hoursUntil > 1 and minutesUntil < 0:
                # print('Pass2')
                hoursUntil -= 1
                # if str in pierreeventtimes:
                #     eventName = 'Pierre'
                # elif str in gauntleteventtimes:
                #     eventName = 'Halloween Gauntlet'
                if str in dasheventtimes:
                    eventName = 'Winter Dash'
                await ctx.send(f'{eventName} is in {hoursUntil} hour(s) and {60-abs(minutesUntil)} minute(s) at {str}')
                return
            if hoursUntil == 1 and minutesUntil < 0:
                # print('Pass3')
                # if str in pierreeventtimes:
                #     eventName = 'Pierre'
                # elif str in gauntleteventtimes:
                #     eventName = 'Halloween Gauntlet'
                if str in dasheventtimes:
                    eventName = 'Winter Dash'
                await ctx.send(f'{eventName} is in {60-abs(minutesUntil)} minute(s) at {str}')
                return
        elif hoursUntil == 0 and minutesUntil > 0:
            # print('Pass4')
            # if str in pierreeventtimes:
            #         eventName = 'Pierre'
            # elif str in gauntleteventtimes:
            #     eventName = 'Halloween Gauntlet'
            if str in dasheventtimes:
                eventName = 'Winter Dash'
            await ctx.send(f'{eventName} is in {minutesUntil} minute(s) at {str}')
            return
    # Accounts for {eventName} occuring on the next day
    eHour = int(alleventtimes[0][0:2])
    eMinute = int(alleventtimes[0][3:5])
    hoursUntil = eHour+24-sHour
    minutesUntil = eMinute-sMinute
    str = alleventtimes[0]

    if hoursUntil > 0:
        if minutesUntil >= 0:
            # print('Pass5')
            # if str in pierreeventtimes:
            #     eventName = 'Pierre'
            # elif str in gauntleteventtimes:
            #     eventName = 'Halloween Gauntlet'
            if str in dasheventtimes:
                eventName = 'Winter Dash'
            await ctx.send(f'{eventName} is in {hoursUntil} hour(s) and {minutesUntil} minute(s) at {str}')
            return
        if hoursUntil > 1 and minutesUntil < 0:
            # print('Pass6')
            hoursUntil -= 1
            # if str in pierreeventtimes:
            #     eventName = 'Pierre'
            # elif str in gauntleteventtimes:
            #     eventName = 'Halloween Gauntlet'
            if str in dasheventtimes:
                eventName = 'Winter Dash'
            await ctx.send(f'{eventName} is in {hoursUntil} hour(s) and {60-abs(minutesUntil)} minute(s) at {str}')
            return
        if hoursUntil == 1 and minutesUntil < 0:
            # print('Pass7')
            # if str in pierreeventtimes:
            #     eventName = 'Pierre'
            # elif str in gauntleteventtimes:
            #     eventName = 'Halloween Gauntlet'
            if str in dasheventtimes:
                eventName = 'Winter Dash'
            await ctx.send(f'{eventName} is in {60-abs(minutesUntil)} minute(s) at {str}')
            return
    elif hoursUntil == 0 and minutesUntil > 0:
        # print('Pass8')
        # if str in pierreeventtimes:
        #     eventName = 'Pierre'
        # elif str in gauntleteventtimes:
        #     eventName = 'Halloween Gauntlet'
        if str in dasheventtimes:
                eventName = 'Winter Dash'
        await ctx.send(f'{eventName} is in {minutesUntil} minute(s) at {str}')
        return
    

####################################################################################

# Orbis etc. GUIDE
@bot.command(name='orbisetc',help='Displays Orbis Etc. Guide')
async def orbisetc(ctx):
    await ctx.send(file=discord.File(dir_path+'/orbisetc.png'))

# Leech GUIDE
@bot.command(name='leech',help='Displays Leech Guide')
async def leech(ctx):
    await ctx.send(file=discord.File(dir_path+'/leech.png'))

# Mage 1hit GUIDE
@bot.command(name='mage1hit',help='Displays Mage Magic 1-hit Breakpoints')
async def mage1hit(ctx):
    await ctx.send(file=discord.File(dir_path+'/mage1hit.jpg'))

# HT HS GUIDE
@bot.command(name='hthp',help='Displays HS Marks for HT Single Target (1024x768')
async def hthp(ctx):
    await ctx.send(file=discord.File(dir_path+'/HTSingleTarget.png'))



# APQ GUIDE
@bot.command(name='apq',help='Displays APQ Guide')
async def apq(ctx):
    #embed = discord.Embed()
    #embed.description = 'https://mapleroyals.com/forum/threads/crimsonwood-party-quest-prequisite-guide-2020-cwpq.153541/'

    await ctx.send(file=discord.File(dir_path+'/apq.png'))

# BF GUIDE
@bot.command(name='bf',help='Displays BF Guide')
async def bf(ctx):
    await ctx.send(file=discord.File(dir_path+'/bf.png'))

# BF GUIDE 2
@bot.command(name='bigfoot',help='Displays Bigfoot Guide by Sparky95')
async def bigfoot(ctx):
    await ctx.send(file=discord.File(dir_path+'/bigfoot.png'))

#################################################################################### PALA
# Pala GUIDE
@bot.command(name='pala',help='Displays BF Guide')
async def pala(ctx):
    await ctx.send(file=discord.File(dir_path+'/pala.png'))

# Pala CWK GUIDE
@bot.command(name='palaCWK',help='Displays Paladin CWK Guide')
async def palacwk(ctx):
    await ctx.send(file=discord.File(dir_path+'/palacwk.png'))

# Pala ZAK GUIDE
@bot.command(name='palaZAK',help='Displays Paladin ZAK Guide')
async def palazak(ctx):
    await ctx.send(file=discord.File(dir_path+'/palazak.png'))

# Pala HT GUIDE
@bot.command(name='palaHT',help='Displays Paladin HT Guide')
async def palaht(ctx):
    await ctx.send(file=discord.File(dir_path+'/palaht.png'))

# Pala NT GUIDE 1
@bot.command(name='palant1',help='Displays Paladin NT Guide 1')
async def palant1(ctx):
    await ctx.send(file=discord.File(dir_path+'/nt1.png'))

# Pala NT GUIDE 2
@bot.command(name='palant2',help='Displays Paladin NT Guide 2')
async def palant2(ctx):
    await ctx.send(file=discord.File(dir_path+'/nt2.png'))

####################################################################################

# Boss Weaknesses 1
@bot.command(name='bossinfo1',help='Displays Boss Info 1')
async def bossinfo1(ctx):
    await ctx.send(file=discord.File(dir_path+'/bossinfo1.png'))

# Boss Weaknesses 2
@bot.command(name='bossinfo2',help='Displays Boss Info 2')
async def bossinfo2(ctx):
    await ctx.send(file=discord.File(dir_path+'/bossinfo2.png'))

# Toad
@bot.command(name='toad',help='Displays Toad Information')
async def toad(ctx):
    await ctx.send(file=discord.File(dir_path+'/toad.png'))

# Boss HP/EXP Info
@bot.command(name='bossexp',help='Displays Boss HP/EXP Info')
async def bossexp(ctx):
    await ctx.send('(taken from hiddenstreet) \nPapulatus: [8.03:1] 23,000,000 HP : 2,860,800 EXP \nZakum: [9.54:1] 482,100,000 HP : 50,498,560 EXP (may not be right exp/ratio) \nKrex: [8.68:1] 500,000,000 HP : 57,600,000 EXP (taken from Joong) \nScarlion/Targa: [15.5:1] 300,000,000 HP : 19,353,600 EXP \nScarlion+Targa (both in corner): [~7.75-11.62:1] ~300,000,000-450,000,000 HP : 37,707,200 EXP \nHorntail: [7.93:1] 2,730,000,000 HP : 344,146,432 EXP (from ilyssia''s chart) \nToad: [6.98:1] 1,070,000,000 HP : 153,120,000 EXP \nThe Boss (total): [7.84:1] 1,050,000,000 HP : 133,760,000 EXP (may not be right exp/ratio) \nShao: [1.95:1] 100,000,000 HP : 51,200,000 EXP')

# HP Quest
@bot.command(name='hpquest',help='Displays HP Quest Info')
async def hpquest(ctx):
    await ctx.send(file=discord.File(dir_path+'/hpquest.png'))


# CWK GUIDE
@bot.command(name='cwk', help='Displays CWK Guide')
async def cwk(ctx):
    embed = discord.Embed()
    embed.description = 'https://mapleroyals.com/forum/threads/crimsonwood-party-quest-prequisite-guide-2020-cwpq.153541/'

    await ctx.send(embed=embed, file=discord.File(dir_path+'/cwk.png'))

# Splits Calculator
@bot.command(name='splits', help='Calculates Splits\n !splits <price> <name of character 1> <name of character 2> <name of character3>...\n For partial splits, you can type (<percentage>) next to the character name\n Ex. !splits 1000000000 dog cat(50) rat')
async def splits(ctx, price, *argv):
    # Value of splitFactor may change if there is a partial split
    splitFactor = []
    currentMemberSplit = []
    index = 0
    partial = False
    partialSplitFactor = 1
    response = ''
    members = (argv)

    try:
        int(price)
    except ValueError:
        await ctx.send('Please enter a valid price, no commas')
        return

    taxedPrice = int(price)*.97
    numMembers = len(members)
    
    memberSplit = int(taxedPrice)//numMembers

    # Check for partial split
    for arg in members:
        # Parentheses in argument indicate there is a partial
        stringArg = str(arg)
        first = stringArg.find('(')
        last = stringArg.find(')')

        # Capture the partial percentage amount of split
        stringArg2 = stringArg[first+1: last]
        
        splitFactor.append(1)
        if first != -1 or last != -1:
            partial = True
            splitFactor[index]=int(stringArg2)/100
            partialSplitFactor = splitFactor[index]
        index += 1

    # Calculate each member's split
    index = 0
    for arg in members:    
        currentMemberSplit.append(int(round(taxedPrice/(numMembers-(1-partialSplitFactor))*splitFactor[index])))
        response += (f'{arg} receives {"{:,}".format(currentMemberSplit[index])} ({currentMemberSplit[index]})\n')
        index += 1

    await ctx.send(f'The total after tax is {"{:,}".format(int(round(taxedPrice)))} ({int(round(taxedPrice))}). \n\n{response}')

# HP Washing Info
@bot.command(name='HPwashInfo', help = 'Displays info for HP Washing')
async def hpwashinfo(ctx):
    #info = ('Here''s some data for HP washing by adding the point to HP using an AP reset, and then removing it using another reset\nJob, HP gained, MP lost, Min MP, Min HP\nBeginner, +8~12HP, -8MP, (10 x level) +2\nSpearman/Paladin, +50~55HP, -4MP, (4 x level) +156\nHero, +50-55HP, -4MP, (4 x level) +56\nThief, +16~20HP (20-24HP Fresh AP), -12MP, (14 x level) +156\nBowman, +16~20HP, -12MP, (14 x level) +148\nMagician, +10~20HP, -90MP, (14 x level) +148\nPirate, +20HP (+40HP for Brawlers), -16MP, (18 x level) +111')
    await ctx.send(file=discord.File(dir_path+'/hpwash.png'))

# HP Washing Calculator
@bot.command(aliases=['wash','washes','hpwash'], help = 'Calculates how many times the character can wash based on their current level and extra MP\n ~hpwash <job> <level> <MP without Equips>')
async def hpwashing(ctx, job, level, mp, *argv):
    #ctx.send('HP Washing Feature is currently under maintenance...')
    #return

    minMP = 0
    aprHP = 0
    minusAprMP = 0
    washedHP = 0
    freshHP = 0
    aprHPmin = 0
    aprHPmax = 0
    freshAP = 0

    try:
        int(level)
    except ValueError:
        await ctx.send('Please enter a valid level\n``~hpwash <job> <level> <MP without Equips>``')
        return
    try:
        int(mp)
    except ValueError:
        await ctx.send('Please enter a valid mp\n``~hpwash <job> <level> <MP without Equips>``')
        return

    try:
        int(argv[0])
    except ValueError:
        await ctx.send('Please enter a valid amount of fresh AP\n``~hpwash <job> <level> <MP without Equips>``')
        return
    except IndexError:
        pass
    else:
        freshAP = int(argv[0])
        pass
    

    level = int(level)
    mp = int(mp)

    if level < 1 or level > 200:
        await ctx.send(f'Your level must be 1-200')
        await ctx.send('``~hpwash <job> <level> <MP without Equips>``')        
        return
    # Here's some data for those who already know about HP Washing:
    # Job, HP gained, MP lost, Min MP, Min HP
    # Beginner, +8~12HP, -8MP, (10 x level) +2, (12 x level) +50
    # Warrior, +50~54HP, -4MP, (4 x level) +156, (24 x level) +172
    # Thief, +20~24HP, -12MP, (14 x level) +156, (24 x level) +472
    # Bowman, +16~20HP, -12MP, (14 x level) +148, (20 x level) +378
    # Magician, +6~10HP, -90MP, (14 x level) +148, (20 x level) +378
    # Pirate, +16~20HP (+36~40HP for Brawlers), -16MP, (18 x level) +111, (22 x level) +380

    # Here's some data for HP washing by adding the point to HP using an AP reset, and then removing it using another reset:
    # Job, HP gained, MP lost, Min MP, Min HP
    # Beginner, +8~12HP, -8MP, (10 x level) +2
    # Spearman/Paladin, +50~55HP, -4MP, (4 x level) +156
    # Hero, +50-55HP, -4MP, (4 x level) +56
    # Thief, +16~20HP (20-24HP Fresh AP), -12MP, (14 x level) +156
    # Bowman, +16~20HP, -12MP, (14 x level) +148
    # Magician, +10~20HP, -90MP, (14 x level) +148
    # Pirate, +20HP (+40HP for Brawlers), -16MP, (18 x level) +111
    accepted_strings_Warrior = ['warrior','swordman','fighter','crusader','hero','page','whiteknight','paladin','pala','pally','spearman','dragonknight','darkknight','dk']
    accepted_strings_Warrior2 =['fighter','crusader','hero']
    accepted_strings_Archer = ['archer','bowman','hunter','ranger','bowmaster','bm','crossbowman','crossbowwoman','sniper','marksman','mm']
    accepted_strings_Thief = ['thief','rogue','assassin','sin','hermit','nightlord','nl','bandit','dit','chiefbandit','cb','shadower','shad']
    accepted_strings_Brawler = ['brawler','marauder','buccaneer','bucc']
    accepted_strings_Sair = ['gunslinger','slinger','outlaw','corsair','sair']
    accepted_strings_Mage = ['magician','cleric','priest','bishop','bish','bs','wizard','mage','archmage','am']

    if job in accepted_strings_Warrior:
        minMP = level*4+156
        if job in accepted_strings_Warrior2:
            minMP = level*4*56
        aprHPmin = 50
        aprHPmax = 55
        aprHP = 53
        minusAprMP = 4
    elif job in accepted_strings_Archer:
        minMP = level*14+148
        aprHPmin = 16
        aprHPmax = 20
        aprHP = 18
        minusAprMP = 12
    elif job in accepted_strings_Thief:
        minMP = level*14+156
        aprHPmin = 16
        aprHPmax = 20
        aprHP = 18
        freshHPmin = 20
        freshHPmax = 24
        freshHP = 22
        minusAprMP = 12
    elif job in accepted_strings_Brawler:
        minMP = level*18+111
        aprHPmin = 40
        aprHPmax = 40
        aprHP = 40
        minusAprMP = 16
    elif job in accepted_strings_Sair:
        minMP = level*18+111
        aprHPmin = 40
        aprHPmax = 40
        aprHP = 20
        minusAprMP = 16
    elif job in accepted_strings_Mage:
        minMP = level*22+488
        aprHPmin = 10
        aprHPmax = 20
        aprHP = 15
        minusAprMP = 30
    else:
        sep = ""
        await ctx.send('Please state the job correctly')
        await ctx.send(f'Acceptable jobs are: \n{*accepted_strings_Warrior, sep}\n{*accepted_strings_Archer, sep}\n{*accepted_strings_Thief, sep}\n{*accepted_strings_Brawler, sep}\n{*accepted_strings_Sair, sep}\n{*accepted_strings_Mage, sep}')
        await ctx.send('``~hpwash <job> <level> <MP without Equips>``')
        return
        #{*accepted_strings_Archer, sep = ", "}\n{*accepted_strings_Thief, sep = ", "}\n{*accepted_strings_Brawler, sep = ", "}\n{*accepted_strings_Sair, sep = ", "}\n{*accepted_strings_Mage, sep = ", "}

    numAPRs = int(round((mp-minMP)/minusAprMP))
    if numAPRs <= 0:
        numAPRs = 0
        washedHP = 0
        await ctx.send(f'You cannot wash based on these credentials')
        return

    washedHPmin = aprHPmin*numAPRs
    washedHPmax = aprHPmax*numAPRs        
    washedHP = aprHP*numAPRs

    # Pirates get a static 40 HP from aprs
    if job in accepted_strings_Brawler or job in accepted_strings_Sair:
        await ctx.send(f'**This feature is still currently being tested**\nYour minimum MP is {"{:,}".format(minMP)}\nYour extra mp is {"{:,}".format(mp-minMP)}\nYou can wash with APR {"{:,}".format(numAPRs)} times and gain an approximate of **{"{:,}".format(washedHP)}** HP')
        return
    
    # Return statement for non-pirates
    await ctx.send(f'**This feature is still currently being tested**\nYour minimum MP is {"{:,}".format(minMP)}\nYour extra mp is {"{:,}".format(mp-minMP)}\nYou can wash with APR {"{:,}".format(numAPRs)} times and gain {"{:,}".format(washedHPmin)} - {"{:,}".format(washedHPmax)} **({"{:,}".format(washedHP)} average)** HP')
    
    # If user wants to wash thief with fresh AP first before APR    
    if job in accepted_strings_Thief and freshAP > 0:
        washedfreshHPmin = freshAP * freshHPmin
        washedfreshHPmax = freshAP * freshHPmax
        washedfreshHP = freshAP * freshHP
        mp = mp-freshAP*minusAprMP
        numAPRs = int(round((mp-minMP)/minusAprMP))
        washedHPmin = aprHPmin*numAPRs
        washedHPmax = aprHPmax*numAPRs        
        washedHP = aprHP*numAPRs

    # Extra return for thieves
    if job in accepted_strings_Thief and freshAP > 0:
        await ctx.send(f'||As a thief, you can wash with fresh AP up to {"{:,}".format(freshAP)} times and gain {"{:,}".format(washedfreshHPmin)} - {"{:,}".format(washedfreshHPmax)} **({"{:,}".format(washedfreshHP)} average)**\nYou can then wash with APRs up to {"{:,}".format(numAPRs)} times and gain {"{:,}".format(washedHPmin)} - {"{:,}".format(washedHPmax)} **({"{:,}".format(washedHP)} average)** HP\nTotal HP gained from this method: {"{:,}".format(washedfreshHPmin + washedHPmin)} - {"{:,}".format(washedfreshHPmax + washedHPmax)} **({"{:,}".format(washedfreshHP+washedHP)} average)** HP||')
        return
    if job in accepted_strings_Thief:
        await ctx.send(f'If you plan to wash with Fresh AP as well, you may use the command below\n~hpwash thief <level> <MP without equips> <# of fresh AP>')

#Physical Damage Range Calculator
@bot.command(name = 'attrange', help = 'Calculates the attack range given the weapon, str, dex, int, luk, and weapon attack\nAvailable weapons are: 1hsword, 2hsword, 1haxe, 2haxe, 1hbw, 2hbw, spear, polearm, dagger, claw, bow, xbow, knuckle, gun')
async def attrange(ctx, wep: str, strx: float, dexx: float, intx: float, lukx: float, wattx: float):
    if wep == '1hsword':
        maxprimary = strx * 4.0
        minprimary = maxprimary
        secondary = dexx
        mastery = 0.6
    elif wep == '1haxe' or wep == '1hbw':
        maxprimary = strx * 4.4
        minprimary = strx * 3.2
        secondary = dexx
        mastery = 0.6
    elif wep == '2hsword':
        maxprimary = strx * 4.8
        minprimary = strx * 4.6
        secondary = dexx
        mastery = 0.6
    elif wep == '2haxe' or wep == '2hbw':
        maxprimary = strx * 4.8
        minprimary = strx * 3.4
        secondary = dexx
        mastery = 0.6
    elif wep == 'spear' or wep == 'polearm':
        maxprimary = strx * 5.0
        minprimary = strx * 3.0
        secondary = dexx
        mastery = 0.8
    elif wep == 'dagger' or wep == 'claw':
        maxprimary = lukx * 3.6
        minprimary = maxprimary
        secondary = strx + dexx
        mastery = 0.6
    elif wep == 'bow':
        maxprimary = dexx * 3.4
        minprimary = maxprimary
        secondary = strx
        mastery = 0.9
    elif wep == 'xbow':
        maxprimary = dexx * 3.6
        minprimary = maxprimary
        secondary = strx
        mastery = 0.9
    elif wep == 'knuckle':
        maxprimary = strx * 4.8
        minprimary = maxprimary
        secondary = dexx
        mastery = 0.6
    elif wep == 'gun':
        maxprimary = dexx * 3.6
        minprimary = maxprimary
        secondary = strx
        mastery = 0.6
    else:
        await ctx.send('Invalid weapon. Available weapons are: 1hsword, 2hsword, 1haxe, 2haxe, 1hbw, 2hbw, spear, polearm, dagger, claw, bow, xbow, knuckle, gun')
        return
    min = math.floor((minprimary * 0.9 * mastery + secondary) * wattx/100)
    max = math.floor((maxprimary + secondary) * wattx/100)
    await ctx.send(f'{min} ~ {max}')

@bot.command(name = 'whatdrops', help = 'Displays what monster drops a certain item')
async def whatdrops(ctx, *args):
    f = open(dir_path+"/mobs.json","r", encoding = "utf-8")
    data = json.load(f)
    f.close()
    msg = ""
    item = ""
    for arg in args:
        item = item + arg + ' '
    item = item.strip().lower()

    for detail in data:
        drops = detail["drops"]
        for drop in drops:
            if item == drop['name'].lower():
                msg = msg + detail["name"] + ", "
    if msg == '':
        await ctx.send(f'Nothing drops {item}')
    else:
        msg = msg[:-2]
        await ctx.send(msg)

@bot.command(name = 'whatis', help = 'Displays mob information')
async def whatis(ctx, *args):
    mob = ""
    for arg in args:
        mob = mob+arg + ' '
    mob = mob.strip()
    mobName = mob.replace(" ","").lower()
    # mobImage = Image.open(dir_path+'/mobs/'+mobName+'.gif')
    try:
        await ctx.send(file=discord.File(dir_path+'/mobs/'+mobName+'.gif'))
    except FileNotFoundError:
        await ctx.send(f"{mob} is not in the database.")
        return
    f = open(dir_path+"/mobs.json","r", encoding = "utf-8")
    data = json.load(f)
    f.close()
    drops = ""
    for detail in data:
        if mobName == str(detail["name"]).replace(" ","").lower():
            moob = str(detail["name"])
            dropTab = detail["drops"]
            for drop in dropTab:
                drops = drops + drop["name"] + ", "
            drops = drops[:-2]
            break
    desc = "N/A"
    if mobName == "splats":
        desc = "Problem child"
    if mobName == "xves":
        desc = "Finisher of goals. Responds to \"God\" or \"Mine Idol\""
    if mobName == "blacephalon":
        desc = "Keep eat"
    if mobName == "uouoy":
        desc = "87"
    if mobName == "soladuck":
        desc = "Naughty"
    if mobName == "loaft":
        desc = "Evolved Monkey"
    if mobName == "gewn":
        desc = "Cat Lover"
    m = await ctx.send(f'Name: {moob}\nDescription: {desc}\nDrops: {drops}')
    if mobName == "xves" or mobName == "uouoy" or mobName == "loaft":
        await m.add_reaction(discord.utils.get(bot.emojis, name = 'Fk'))

# Credits
@bot.command(name = 'credits', help = 'Lists contributors of this project')
async def credits(ctx):
    credit = """
    Doo (Xves) for providing lots of details and images
    **For providing improvements and suggestions:**
    Joe (Blacephalon)
    Edi (Splats)
    John (HolyRice)
    Bun (Sharpay)
    Chris (DripBrew)
    Nicky (nickybuccc)
    """
    await ctx.send(credit)
bot.run(TOKEN)
