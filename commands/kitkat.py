import discord
from discord.ext import commands

class KitKat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kitkat(self, ctx):
        await ctx.send("LuKy c'est le plus fort ;)")

def setup(bot):
    bot.add_cog(KitKat(bot))
