import discord
from discord.ext import commands
import os

TOKEN = os.environ('BOT_TOKEN')
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(client.user.name,'Is Ready!')

client.run(TOKEN)
