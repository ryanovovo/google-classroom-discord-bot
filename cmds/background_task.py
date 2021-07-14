import discord
from core.classes import CogExtension
import asyncio


class Notification(CogExtension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def interval():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                anc_channel = self.bot.get_channel(self.anc_ch)
                for course in self.cls.list_course():
                    print(course)
                    for anc in self.cls.list_anc(name=course['name']):
                        if anc['id'] not in self.is_send:
                            self.is_send.add(anc['id'])
                            embed = discord.Embed(title=f'{course["name"]}公告', description=anc['text'], color=0x00fcff)
                            await anc_channel.send(embed=embed)
                await asyncio.sleep(5)
        self.bg_task = self.bot.loop.create_task(interval())


def setup(bot):
    bot.add_cog(Notification(bot))