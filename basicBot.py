# Basic packages to import
import os
import discord
from discord import channel
from discord.ext import commands, tasks
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Initialize bot. 
bot = commands.Bot(command_prefix='1', case_insensitive = True)
dir_path = os.path.dirname(os.path.realpath(__file__))
print('Running...')

@bot.event
async def on_ready():
    print('Bot is ready.')
    await bot.change_presence(activity=discord.Game(name='MapleStory'))

bot.run(TOKEN)