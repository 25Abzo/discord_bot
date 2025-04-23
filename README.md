# 🤖 Discord Tech News Bot

Un bot Discord simple et efficace pour recevoir les dernières actualités technologiques issues de [Hacker News](https://news.ycombinator.com/).

---

## 🚀 Fonctionnalités

- `/news` : Récupère les 5 dernières actualités tech de Hacker News.
- Affichage structuré et lisible dans les salons Discord.
- Utilise les **slash commands** pour une meilleure expérience utilisateur.

---

## 🧰 Stack technique


- Python 3.10+
- [discord.py](https://discordpy.readthedocs.io/)
- [Hacker News API](https://github.com/HackerNews/API)
- requests

---

## ⚙️ Installation

1. **Clone le dépôt :**
   ```bash
   git clone https://github.com/25Abzo/discord_bot.git
   cd discord_bot

2. **Installe les dépendances :**
   ```bash
   pip install -r requirements.txt

3. **Ajoute ton token Discord dans un fichier .env:**
   ```env 
   DISCORD_BOT_TOKEN=token

4. **Lance le bot :**
   ```bash
   python main.py
