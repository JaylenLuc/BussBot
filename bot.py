# bot.py

import os
import asyncio
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
        await member.dm_channel.send(f"Welcome {member.name}! The community of Absuridist Boy Pussy is a shoal of diverse groups of people with disparate life experiences that just so happened to cross paths with the King of Boy Pussy and somehow made it as far as to get invited to his server. Find the state of calm, you will find altruism.")

#get this to work
#get predictive text to work
#


def determine_time_msg(bday) -> str:
    now,today = datetime.datetime.now(), datetime.date.today()
    delta = bday - datetime.date.today()
    day_s= ''
    hour_s = ''
    min_s = ''
 
    now_hour = datetime.datetime.now().hour 

    now_days = (365 + delta.days) % 365 
    
    now_minutes = datetime.datetime.now().minute
    msg = ''
    print(delta.days)
    day_str = ''
    now_days = delta.days
    if delta.days == 0:
        return f'Happy Birthday !!!! One day closer to astral projection'
        
    else:
        if delta.days > 1 or delta.days < 0:
            day_s = 's'
        if delta.days > 1:
            day_str = f'{delta.days-1} day{day_s} '
            now_days = 1 
        if now_days == 1:
            now_hour = 24 - now_hour
            now_days = ''
            if now_hour > 1:
                if now_hour -1 <= 1: hour_s = ''
                else: hour_s = 's'                      
                now_minutes = 60 - now_minutes
                if now_minutes > 1: min_s = 's'
                else: min_s = ''
                return day_str + f'{now_hour-1} hour{hour_s} {now_minutes} minute{min_s} until your government age is ${{current_government_age}} + 1 !!!!!'
            
            elif now_hour == 1:
                if now_minutes == 0:
                    now_minutes = 60
                else:
                    now_minutes = 60 -  now_minutes
                if now_minutes > 1: min_s = 's'
                if now_minutes == 1:
                    return day_str +f'1 more Minute until your government age is ${{current_government_age}} + 1 !!!!!'
                return f'{now_minutes} minute{min_s} until your government age is ${{current_government_age}} + 1 !'
            
        if delta.days < 0:
            now_hour = (24 - now_hour) + (24*((365 + (delta.days-1)) % 365))%24
            return f'{now_days} day{day_s} {now_hour-1} hour{hour_s} {now_minutes} minute{min_s} until your government age is ${{current_government_age}} + 1 !!!!!'

        




cont = ''
@bot.command(name = 'bday-countdown', pass_context=True)
async def _bday(ctx, item : typing.Literal['Jane', 'Jask', "Jaylen","Edwin"]):
     
    global b_day
    global b_month
    cont = ctx
    print(cont)
    bday = ''
    if (item == 'Jaylen'):
        #await ctx.send("April 7th 2002")i
        b_day = 7
        b_month = 4
        bday = datetime.date(datetime.datetime.now().year,4,7)
    elif (item == 'Edwin'):
        #await ctx.send("April 7th 2002")i
        b_day = 23
        b_month = 6
        bday = datetime.date(datetime.datetime.now().year,6,23)

    elif (item == 'Jask'):
        #await ctx.send("September 16th 2002")b_month
        b_day = 16
        b_month = 9
        bday = datetime.date(datetime.datetime.now().year,9,16)

    elif (item == 'Jane'):
        b_day = 11
        b_month = 5
        bday = datetime.date(datetime.datetime.now().year,5,11)
            
    mensage = determine_time_msg(bday)
    global bday_msg
    bday_msg = await ctx.send(mensage)
    if mensage == 'Happy Birthday !!!! One day closer to astral projection':
        user = bot.get_user(ctx.message.author.id)
        await user.send("Love u a lot and hope u have a peaceful birthday - Jaylen ")
        return 
    print(bday_msg, type(bday_msg))
    await edit_msg_forJane()

async def edit_msg_forJane():
    #_prev = datetime.datetime.now().minute
    #print('cont: ', cont)
    ddate = determine_time_msg(datetime.date(datetime.datetime.now().year,b_month,b_day))
    while ddate != 'Happy Birthday !!!! One day closer to astral projection':
        
        time.sleep(2) 
        msg = await bday_msg.edit(content = ddate)
        #syncio.sleep(15)   
        
        ddate = determine_time_msg(datetime.date(datetime.datetime.now().year,b_month, b_day))

    await bday_msg.edit(content = ddate)
    user = bot.get_user(cont.message.author.id)
    await user.send("Love u a lot and hope u have a peaceful birthday - Jaylen ")

#hope it works edwin
bot.run(TOKEN)


















