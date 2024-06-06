import discord
from discord.ext import commands

class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def message(self, ctx, agenda_message):
        message = await ctx.send(agenda_message)

        for emoji in ["✅", "❌"]:
            await message.add_reaction(emoji)

def setup(bot):
    bot.add_cog(Message(bot))
