import os
import discord
from discord.ext import commands
from discord.ui import Button, View

# If you haven't set up your intents, do so here:
intents = discord.Intents.default()
# For prefix commands, "message content" intent is often needed:
# intents.message_content = True

bot = commands.Bot(command_prefix=",", intents=intents)

@bot.command()
@commands.has_permissions(administrator=True)
async def submit(ctx):
    # Create an embed with a title, description, and color
    embed = discord.Embed(
        title="Submit a game to Uplink Games!",
        description=(
            "Here's a detailed guide on how to submit your game.\n"
            "Make sure you include the following in your submission:\n"
            "1. Game Title\n"
            "2. Short Description\n"
            "3. Tags and Categories\n\n"
            "Click the button below to submit your game."
        ),
        color=discord.Color.purple()  # or any color you like
    )
    
    # Create a button labeled "Submit Your Game"
    button = Button(label="Submit Your Game", style=discord.ButtonStyle.primary)

    # Define what happens when someone clicks the button
    async def button_callback(interaction: discord.Interaction):
        # This is where you'd handle the submission logic
        await interaction.response.send_message(
            "Thanks for clicking the button! Here's where you'd process the submission form.",
            ephemeral=True
        )

    button.callback = button_callback

    # Add the button to a view
    view = View()
    view.add_item(button)

    # Send the embed + button in the channel
    await ctx.send(embed=embed, view=view)

bot.run(os.environ["DISCORD_TOKEN"])
