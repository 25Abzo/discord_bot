import discord
import requests
import asyncio
import os
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext.commands import Bot

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
bot = Bot(command_prefix="/", intents=intents)

HACKER_NEWS_API = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_API = "https://hacker-news.firebaseio.com/v0/item/{}.json"

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")
    # Enregistre les commandes slash
    await bot.tree.sync()

@bot.tree.command(name="news", description="Récupère les dernières actus tech")
async def fetch_news(interaction: discord.Interaction):
    await interaction.response.defer()  # Signale à Discord que tu vas répondre plus tard

    try:
        top_stories = requests.get(HACKER_NEWS_API).json()[:5]  # Top 5 actus
        news_list = []

        for story_id in top_stories:
            story = requests.get(ITEM_API.format(story_id)).json()
            title = story.get("title", "(Sans titre)")
            url = story.get("url", "(Pas de lien)")
            news_list.append(f"**{title}**\n🔗 {url}\n")

        response = "\n".join(news_list)
        await interaction.followup.send(response)

    except Exception as e:
        print("Erreur :", e)
        await interaction.followup.send("❌ Une erreur est survenue lors de la récupération des actus.")

bot.run(TOKEN)
