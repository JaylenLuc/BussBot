# bot.py

import os

import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')[1:-1]
intents = discord.Intents(messages=True, guilds=True)
print(TOKEN)
intents.message_content = True
intents.reactions = True

client = discord.Client(intents=intents)


@client.event

async def on_ready():
    print(f'{client.user} in server {client.guilds[0].name} has connected to Discord :)')

client.run(TOKEN)


















