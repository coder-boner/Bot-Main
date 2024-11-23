import os
import random
import discord
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
from itertools import cycle
import json
import random

# Replace this with your bot's token
TOKEN = 'TOKEN'

#Discord Intents LEAVE ALONE IF IT WORKS
intents = discord.Intents.default()
intents.members = True
intents.typing = True
intents.presences = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents = intents)

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')


# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    print('Bot is ready!')
    status = cycle(["Testing the bot", "placement", "Super skibidi rizz"])

@bot.command() #Command to test embeds
async def embed_test(message):
    embedVar = discord.Embed(title="Server Info", description="The server", color=0x00ff00)
    embedVar.add_field(name="Field1", value="hi", inline=False)
    embedVar.add_field(name="Field2", value="hi2", inline=False)
    await message.channel.send(embed=embedVar)

# Run the bot
bot.run(TOKEN)
