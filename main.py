import discord
import dotenv
import os
from aiohttp import web
from discord.ext import commands

# Load environment variables from .env file
dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Import commands
import bot_commands
bot_commands.setup(bot)
print("All commands loaded successfully.")

# Setup aiohttp web server
from webhooks import webhooks_setup

app = web.Application()

# Register all webhook routes
webhook_map = webhooks_setup(bot)
for name, webhook in webhook_map.items():
    print(f"Loading webhook: {name} on {webhook['path']}")
    app.router.add_route("POST", webhook["path"], webhook["handler"])

# Run bot + web server
async def start_bot():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
    await bot.start(TOKEN)

import asyncio
asyncio.run(start_bot())