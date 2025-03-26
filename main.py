import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# A simple command to test the bot
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Start the bot using the token stored in an environment variable
bot.run(os.environ['MTM1NDU0MjYzOTY0Njc2OTE5Mg.GCJ9FS.18h-lCIO3WbZOySf1hwF8xycF9TPA1pV-qIJ-0'])
