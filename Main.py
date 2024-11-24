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
intents.guilds = True
intents.guild_messages = True
intents.moderation = True
intents.reactions = True

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
    colour = discord.Colour.from_rgb(2, 110, 168)
    embedVar = discord.Embed(title="Server Info", description="The Etheral Foundation Network is a server where we listen to the community and do what they want, we try to make the gaming experience as fun as possible. We do this by having multiple different game modes (Heavily Modded, Vanilla +, ect.) to let everyone have a wide range possible game modes to play. We hope you enjoy playing!", color=colour)
    embedVar.add_field(name="**CONTACT: admin@etheralfn.com**", value="", inline=False)
    embedVar.add_field(name="**APPLY HERE: **https://discord.com/channels/1272058561924435990/1272059372767285300", value="", inline=False)
    embedVar.add_field(name="**READ THE RULES: **https://discord.com/channels/1272058561924435990/1272059312872624191", value="", inline=False)
    embedVar.set_author(name="The Etheral Foundation Network", url="https://i.postimg.cc/3NK1gKVG/serverlogo.webp")
    #embedVar.set_image(url="https://i.postimg.cc/3NK1gKVG/serverlogo.webp")
    embedVar.add_field(name="Website", value="https://etheralfn.com/")
    embedVar.set_thumbnail(
        url="https://i.postimg.cc/3NK1gKVG/serverlogo.webp")
    embedVar.set_footer(text="Made by walter")
    await message.channel.send(embed=embedVar)

    colour = discord.Colour.from_rgb(2, 110, 168)
    embedVar = discord.Embed(title="Management:", description=" ", color=colour)
    embedVar.add_field(name="NETWORK OWNER", value="The <@&1272059235223601244> manages everything with the server and finances the server to expand it. They also find developers and manage all staff.", inline=False)
    embedVar.add_field(name="NETWORK CO OWNER", value="The <@&1272059236599201803> helps the Network Owner with managing and devloping the server.")
    embedVar.add_field(name="DISCORD DIRECTOR", value="The <@&1307877759871225997> manages and develops the discord server and helps out with events ect.", inline=False)
    embedVar.add_field(name="SCP:SL DIRECTOR", value="The <@&1307879130427293757> manages and devlops the SCP:SL Servers and does events on them")
    await message.channel.send(embed=embedVar)

# Run the bot
bot.run(TOKEN)
