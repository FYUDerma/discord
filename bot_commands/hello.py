import discord
from discord.ext import commands

@commands.command()
async def hello(ctx):
    await ctx.send("Hello, World!")

# Add the command to the bot
def setup(bot):
    bot.add_command(hello)