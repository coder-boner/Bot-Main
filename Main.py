import os
import random
import time
import asyncio
import discord
from discord.ext import commands
from discord.ext import tasks
from discord import app_commands
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

OWNER_USER_ID = 769912339255263233

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

restart_count = 0  # Counter for how many times the bot has restarted

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    print('Bot is ready!')

    # Track the start time of the bot
    start_time = time.time()

    while True: #Made by chat gpt since I could not figure out :(
        # Calculate the bot's uptime
        uptime_seconds = int(time.time() - start_time)

        # Calculate time components
        years = uptime_seconds // (365 * 24 * 60 * 60)
        uptime_seconds %= (365 * 24 * 60 * 60)
        months = uptime_seconds // (30 * 24 * 60 * 60)
        uptime_seconds %= (30 * 24 * 60 * 60)
        weeks = uptime_seconds // (7 * 24 * 60 * 60)
        uptime_seconds %= (7 * 24 * 60 * 60)
        days = uptime_seconds // (24 * 60 * 60)
        uptime_seconds %= (24 * 60 * 60)
        hours = uptime_seconds // (60 * 60)
        uptime_seconds %= (60 * 60)
        minutes = uptime_seconds // 60
        seconds = uptime_seconds % 60

        # Format the uptime string
        uptime_string = f"{years}Y {months}M {weeks}W {days}D {hours}H {minutes}M {seconds}S"

        # Update the bot's presence with the formatted uptime
        await bot.change_presence(activity=discord.Game(name=uptime_string))

        # Wait for a second before updating the uptime again
        await asyncio.sleep(1)

@bot.command() #Command to test embeds
async def embed_test(ctx):
    if ctx.author.id == OWNER_USER_ID:
        colour = discord.Colour.from_rgb(2, 110, 168)#Server info in a embed
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
        await ctx.channel.send(embed=embedVar)

        colour = discord.Colour.from_rgb(2, 110, 168) #Management info in a embed
        embedVar = discord.Embed(title="Management:", description=" ", color=colour)
        embedVar.add_field(name="Network Owner", value="The <@&1272059235223601244> manages everything with the server and finances the server to expand it. They also find developers and manage all staff.", inline=False)
        embedVar.add_field(name="Network Co Owner", value="The <@&1272059236599201803> helps the Network Owner with managing and devloping the server.", inline=False)
        embedVar.add_field(name="Discord Director", value="The <@&1307877759871225997> manages and develops the discord server and helps out with events ect.", inline=False)
        embedVar.add_field(name="SCP:SL Director", value="The <@&1307879130427293757> manages and devlops the SCP:SL Servers and does events on them", inline=False)
        embedVar.add_field(name="US Server Hoster", value="The <@&1291980890632622141> Server Hoster is the hoster of the US Servers", inline=False)
        embedVar.add_field(name="AU Server Hoster", value="The <@&1272059237337661471> Server Hoster is the hoster of the AU Servers", inline=False)
        embedVar.add_field(name="Server Manager", value="The <@&1272059240747503649> manages and checks on the Servers to make sure they are working properly", inline=False)
        embedVar.add_field(name="Community Manager", value="The <@&1272059241619787848> manages the community and manges events and other things with the community", inline=False)
        embedVar.add_field(name="Staff Manager", value="The <@&1272059242555375651> manages the entire staff team and decides if people are to be promoted ir let in the staff team", inline=False)
        await ctx.channel.send(embed=embedVar)

        colour = discord.Colour.from_rgb(2, 110, 168) #Developer info in a embed
        embedVar = discord.Embed(title="Developer/Staff:", description=" ", color=colour)
        embedVar.add_field(name="Developers:", value=" ", inline=False)
        embedVar.add_field(name="Wiki Editor", value="The <@&1299740904864874559> manages and changes the wiki", inline=False)
        embedVar.add_field(name="----SL Development Team----", value="The <@&1272059243666739265> is made up of many roles that all work on the SCP:SL Servers to make them better and more fun", inline=False)
        embedVar.add_field(name="----Minecraft Development Team----", value="The <@&1299741070967705662> is made up of many roles that all work on the Minecraft Servers to make them better and more fun", inline=False)
        #Staff
        embedVar.add_field(name="----Staff Team----", value="The <@&1272059253581938780> consists of the <@&1272059254181728369> and <@&1272059258057265166> which all moderate the server to make it more enjoyable", inline=False)
        await  ctx.channel.send(embed=embedVar)

        colour = discord.Colour.from_rgb(2, 110, 168)
        embedVar = discord.Embed(title="Misc Roles:", description=" ", color=colour)
        embedVar.add_field(name="Event Staff", value="The <@&1272059263228837933> do events in game so then you can enjoy playing them with dedicated staff (DO NOT BEG FOR EVENTS IF YOU SEE ONE AS YOU WILL BE MUTED)", inline=False)
        embedVar.add_field(name="Partnered", value="<@&1272059264407437394> are other server owners that have partnered with our server amd have their own channels for announcements, go join their discord.", inline=False)
        embedVar.add_field(name="Bots", value="<@&1272059276411539577> are bots for the server, some are even made by us", inline=False)
        embedVar.add_field(name="QA Tester", value="<@&1272059265787363348> test out servers and server features before they are released to the public so then they are not buggy when released", inline=False)
        embedVar.add_field(name="OG Member", value="<@&1272059269210050610> have been here since the start, and is now unobtainable", inline=False)
        embedVar.add_field(name="Member", value="<@&1272059274989797419> are members", inline=False)
        await ctx.channel.send(embed=embedVar)


    else:
        await ctx.reply(f"{ctx.author.mention} You are not allowed to use this command!")



# Run the bot
bot.run(TOKEN)
