import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=",")

@bot.event
async def on_ready():
  print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
  await ctx.send("Pong")

bot.run(os.environ('MTM1NDU0MjYzOTY0Njc2OTE5Mg.GCJ9FS.18h-lCIO3WbZOySf1hwF8xycF9TPA1pV-qIJ-0')
