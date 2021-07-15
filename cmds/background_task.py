import discord
from discord.ext import tasks
from core.classes import CogExtension
import asyncio


class Notification(CogExtension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_send.load_data()

        async def send_anc(course):
            anc_channel = self.bot.get_channel(self.anc_ch)
            for anc in self.cls.list_anc(name=course['name']):
                if not self.is_send.find(anc['id']):
                    # print(anc)
                    self.is_send.push(anc['id'])
                    self.is_send.save_data()
                    embed = discord.Embed(title=f'{course["name"]}公告', description=anc['text'], url=anc['alternateLink'],color=0x00fcff)
                    await anc_channel.send(embed=embed)

        async def send_hw(course):
            hw_channel = self.bot.get_channel(self.hw_ch)
            for hw in self.cls.list_hw(name=course['name']):
                if not self.is_send.find(hw['id']):
                    self.is_send.push(hw['id'])
                    self.is_send.save_data()
                    des = hw.get('description', '\u200b')
                    if len(des) > 1000:
                        des = des[0:1000]
                        des = des + "..."
                    embed = discord.Embed(title=f'{course["name"]}作業', url=hw['alternateLink'], color=0xff9200)
                    embed.add_field(name=hw['title'], value=des, inline=False)
                    await hw_channel.send(embed=embed)

        async def interval():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                courses = self.cls.list_course()
                for course in courses:
                    await send_hw(course)
                    await send_anc(course)

                await asyncio.sleep(10)

        self.bg_task = self.bot.loop.create_task(interval())


def setup(bot):
    bot.add_cog(Notification(bot))
