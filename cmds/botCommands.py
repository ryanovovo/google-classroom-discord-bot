from core.classes import CogExtension
from discord.ext import commands
import discord
from cmds.background_task import Notification


class BotCommands(CogExtension):
    @commands.command()
    async def stop(self, ctx):
        embed = discord.Embed(title="Bot Stopped!!!", color=0xff2600)
        await ctx.send(embed=embed)
        exit()


def setup(bot):
    bot.add_cog(BotCommands(bot))


