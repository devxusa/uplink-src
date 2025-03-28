import os
import discord
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=",", intents=intents)

@bot.command()
@commands.has_permissions(administrator=True)
async def submit(ctx):
    embed = discord.Embed(
        title="Submit a game to Uplink Games!",
        description=(
            "Here's a detailed guide on how to submit your game.\n"
            "Make sure you include the following in your submission:\n"
            "1. Game Title\n"
            "2. Short Description\n"
            "3. Tags and Categories\n\n"
            "⚠️WARNING⚠️ We are investigating the issue with the images. Please do NOT upload an image with your game, we will automatically add one."
            "Click the button below to submit your game."
        ),
        color=discord.Color.purple()
    )
    
    button = Button(label="Submit Your Game", style=discord.ButtonStyle.link, url="https://polyoids.com/upload")
    view = View()
    view.add_item(button)
    
    await ctx.send(embed=embed, view=view)

bot.run(os.environ["DISCORD_TOKEN"])
