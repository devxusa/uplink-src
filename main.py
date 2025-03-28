import os
import discord
from discord.ext import commands
from flask import Flask
import threading

# Set up a minimal Flask app to keep the process alive
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is up and running!"

def run():
    app.run(host='0.0.0.0', port=5000)

threading.Thread(target=run).start()

# Define your intents
intents = discord.Intents.default()
# Enable any privileged intents if you need them, for example:
# intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
    
bot.run(os.environ["DISCORD_TOKEN"])
