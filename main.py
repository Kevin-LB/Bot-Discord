import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

bot.load_extension('commands.agenda')
bot.load_extension('commands.message')

bot.run('votre_token_discord')
