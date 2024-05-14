import os
import discord
from discord.ext import commands
from datetime import datetime, timedelta
import calendar

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def agenda(ctx):
  today = datetime.utcnow() + timedelta(hours=2)
  day_name = calendar.day_name[today.weekday()]
  month_name = calendar.month_name[today.month]
  formatted_date = f"{day_name} {today.strftime('%d')} {month_name}"

  agenda_message = f"**{formatted_date}**\n\n"

  await ctx.send(agenda_message)

  time_slots = [
      "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00 / 23:00"
  ]

  for time_slot in time_slots:
    await message(ctx, f"{time_slot}\n")

  role_mention = ctx.guild.get_role(1238986475471638639)
  if role_mention:
    await ctx.send(role_mention.mention)

  await ctx.send(ctx.author.mention)

@bot.command()
async def message(ctx, agenda_message):
  message = await ctx.send(agenda_message)

  for emoji in ["✅", "❌"]:
    await message.add_reaction(emoji)

token = 'MTIzOTE4NTg5ODY1NTA1NTg5Mg.GOysL-.r5P8PJqpyIZ3jy20C0z9bL6qyD2FG51WsSGpZ4'
token = os.getenv('DISCORD_TOKEN', token)
bot.run(token)
