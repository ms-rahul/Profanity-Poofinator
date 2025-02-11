import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Get the bot token from the environment variables
token = os.getenv("discord_bot_token")

# Create a bot instance with required permissions
intents = discord.Intents.default()
intents.message_content = True  # Allow reading message content
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Check if the message contains only +, -, or *
    if all(char in "+-* " for char in message.content):
        if message.content.strip():
            await message.delete()

    await bot.process_commands(message)

# Start the bot with the token from the .env file
bot.run(token)
