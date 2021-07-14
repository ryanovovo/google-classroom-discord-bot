import discord
from discord.ext import commands, tasks
from classroom import Classroom
import json


with open("setting.json", "r", encoding="utf8") as jfile:
    setting = json.load(jfile)


class CogExtension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cls = Classroom()
        self.is_send = set()
        self.anc_ch = int(setting['anc_channel'])
        self.hw_ch = int(setting['hw_channel'])
