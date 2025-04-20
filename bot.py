import discord
from discord.ext import commands
import os
import json
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('BOT_TOKEN')
prefix = os.getenv('BOT_PREFIX')

PREFIX_FILE = 'prefixes.json'
if os.path.exists(PREFIX_FILE):
    with open(PREFIX_FILE, 'r') as f:
        prefixes = json.load(f)
else:
    prefixes = {}

def save_prefixes():
    with open(PREFIX_FILE, 'w') as f:
        json.dump(prefixes, f, indent=4)



def get_prefix(bot, message):
    return prefixes.get(str(message.guild.id), prefix)


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=get_prefix, intents = intents)



@bot.event
async def on_ready():
    print("==========================")
    print(f"Connected as {bot.user.name}#{bot.user.discriminator}")
    print("==========================")

@bot.command(name="ping")
async def ping(ctx):
    """This returns the bot ping"""
    await ctx.send(f"Pong!\nLatency: {round(bot.latency * 1000)}ms")   

@bot.command(name='prefix', aliases=['p'])
async def setprefix(ctx, new_prefix):
    prefixes[str(ctx.guild.id)] = new_prefix
    save_prefixes()
    await ctx.send(f"Prefix changed to: `{new_prefix}`.")



# @bot.command(name="help")
# async def help(ctx):
#     await ctx.send(f"This is a help command for '{bot.user.name}'")   

bot.run(token)

