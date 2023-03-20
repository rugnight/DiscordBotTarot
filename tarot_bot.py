import discord
import json
import os
import random
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.command(name="tarot")
async def tarot(ctx):
    with open("tarot_cards.json", "r", encoding="utf-8") as f:
        cards = json.load(f)

    selected_card = random.choice(cards)

    embed = discord.Embed(title=selected_card["name"], description=selected_card["description"], color=0x00ff00)
    embed.set_image(url=selected_card["image_url"])

    await ctx.send(embed=embed)

bot.run(TOKEN)





