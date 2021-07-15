import discord
from discord.ext import tasks
from core.classes import CogExtension
import asyncio


class Notification(CogExtension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        @tasks.loop(seconds=0)
        async def send_announcements(course):
            anc_channel = self.bot.get_channel(self.anc_ch)
            for anc in self.cls.list_anc(name=course['name']):
                if anc['id'] not in self.is_send:
                    # print(anc)
                    self.is_send.add(anc['id'])
                    embed = discord.Embed(title=f'{course["name"]}公告', description=anc['text'], color=0x00fcff)
                    await anc_channel.send(embed=embed)

        @tasks.loop(seconds=0)
        async def send_hws(course):
            hw_channel = self.bot.get_channel(self.hw_ch)
            for hw in self.cls.list_hw(name=course['name']):
                # print(hw)
                if hw['id'] not in self.is_send:
                    self.is_send.add(hw['id'])
                    des = hw.get('description', '\u200b')
                    if len(des) > 1000:
                        des = des[0:1000]
                        des = des + "..."
                    embed = discord.Embed(title=f'{course["name"]}作業', url=hw['alternateLink'], color=0xff9200)
                    embed.add_field(name=hw['title'], value=des, inline=False)
                    await hw_channel.send(embed=embed)

        @tasks.loop(seconds=5)
        async def interval():
            await self.bot.wait_until_ready()

            while not self.bot.is_closed():
                courses = self.cls.list_course()
                for course in courses:
                    await send_hws(course)
                    await send_announcements(course)

        interval.start()


def setup(bot):
    bot.add_cog(Notification(bot))
