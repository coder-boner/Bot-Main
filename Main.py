import discord
from discord.ext import commands

# Replace this with your bot's token
TOKEN = 'TOKEN'

intents = discord.Intents.default()
intents.members = True  # To detect members joining/leaving the server

bot = commands.Bot(command_prefix="!", intents=intents)


# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    print('Bot is ready!')

# Run the bot
bot.run(TOKEN)
