# bot.py

import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
import time
import datetime
import  typing

load_dotenv()


cat = """'''            \*            \,MMM8&&&.            *\n\
                         MMMM88&&&&&    .\n\
                        MMMM88&&&&&&&\n\
                \*      MMM88&&&&&&&&\n\
                        MMM88&&&&&&&&\n\
                        \'MMM88&&&&&&\'\n\
                          \'MMM8&&&\'      \*\n\
      |\\\_\_\_/|\n\
    =) ^Y^ (=            .              \'\n\
     \  ^  /\n\
      )=\*=(       \*\n\
     /     \\\n\
     |     |\n\
    /| | | |\\\n\
    \| | |\_|/\n\
  /\\_\_/\\_\_/\\     \n\
           \\_)   ''"""


print(cat)

TOKEN = os.getenv('DISCORD_TOKEN')[1:-1]
GUILD = os.getenv('DISCORD_GUILD')[1:-1]
GUILD_ID = os.getenv('DISCORD_ID')[1:-1]
print(TOKEN)
print(GUILD)
print(GUILD_ID)
intents = discord.Intents(messages=True, guilds=True)
intents.message_content = True
intents.reactions = True
intents.members = True 
client = discord.Client(command_prefix='/',intents=intents)
bot = commands.Bot(command_prefix='/', intents=intents)

channel = ''


@bot.event

async def on_ready():
    
    
    print(f'{client.user} in server {client.guilds} has connected to Discord :)')
    print(client.guilds)
    channel = client.get_channel(GUILD_ID)
    print(channel)                          
@bot.event

async def on_member_join(member):
    print(f"works on join for {member.name}")
    await member.create_dm()
    if (hash(member.name) % 2 == 0):
        await member.dm_channel.send(f"Welcome {member.name} to the Isocratic community of Absurdist Boy pussy, but not in a floccinaucinihilipilificationary sense but in a post modernist, nihilist, main character God complex anti consumerist, luditean, ghadaffi sympathetic, post-kantian schopenhauerian transcendentalist, neurotic self-abosrbed anxious thought-loop sense " +'\n' + cat)
    else:
        await member.dm_channel.send(f"Welcome {member.name}!, the community of Absuridist Boy Pussy is a community of diverse groups of people with disparate life experiences that just so happens to cross paths with the King of Boy Pussy and somehow made it as far to get invited to his server. Find the state of calm, you will find altruism.")


@bot.command(name = 'bday')
async def _bday(ctx, item : typing.Literal['Jane', 'Jask', "Jaylen"]):
    
    if (item == 'Jaylen'):
        await ctx.send("April 7th 2002")
    elif (item == 'Jask'):
        await ctx.send("September 16th 2002")
    elif (item == 'Jane'):
        await ctx.send("May 11th 2000")


#@bott.command()
#async def joined(ctx, *, member: discord.Member):
#        await ctx.send(f'{member} joined on {member.joined_at}i !!!!')

bot.run(TOKEN)


















