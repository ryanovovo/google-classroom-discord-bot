import discord
from discord.ext import commands, tasks
from classroom import Classroom
from core.classes import CogExtension


class Checkinfo(CogExtension, discord.Client):
    @commands.command()
    async def listcourses(self, ctx):
        embed = discord.Embed(title="所有課程", color=0x00f900)
        courses = self.cls.list_course()
        for course in courses:
            embed.add_field(name=course['name'], value='\u200b', inline=False)
            print(course)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Checkinfo(bot))