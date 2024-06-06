import discord
from discord.ext import commands
from datetime import datetime, timedelta
import calendar

class Agenda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def agenda(self, ctx):
        today = datetime.utcnow() + timedelta(hours=2)
        day_name = calendar.day_name[today.weekday()]
        month_name = calendar.month_name[today.month]
        formatted_date = f"{day_name} {today.strftime('%d')} {month_name}"

        agenda_message = f"**{formatted_date}**\n\n"
        await ctx.send(agenda_message)

        time_slots = [
            "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"
        ]

        for time_slot in time_slots:
            await ctx.invoke(self.bot.get_command("message"), f"{time_slot}\n")

        role_mention = ctx.guild.get_role(1238986475471638639)
        if role_mention:
            await ctx.send(role_mention.mention)

        await ctx.send(ctx.author.mention)

def setup(bot):
    bot.add_cog(Agenda(bot))
