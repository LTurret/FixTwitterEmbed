from os import getenv

from dotenv import load_dotenv

from interactions import listen
from interactions import Client
from interactions import Intents


load_dotenv()

bot = Client(intents=Intents.ALL)


@listen()
async def on_startup():
    print("Bot is running!")


bot.load_extension("EmbedFix")

print("Starting...")

bot.start(getenv("BOT_TOKEN"))
