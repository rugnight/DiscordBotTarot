import os
import random
import discord
from dotenv import load_dotenv
from discord import Intents

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

tarot_cards = [
    # ここにタロットカードのリストを追加してください。
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement",
    "The World"
]

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print(message)
    #print(f'Message received from {message.author}: {message.content} (Type: {message.type})')  # メッセージタイプの出力を追加
    if message.author == client.user or message.type != discord.MessageType.default:  # メッセージタイプのチェックを追加
        return

    if message.content.lower() == '!tarot':
        card = random.choice(tarot_cards)
        response = f'Your tarot card is: {card}'
        await message.channel.send(response)

client.run(TOKEN)
