import discord
from discord.ext import commands, tasks
from classroom import Classroom
import json
from database import DbQueue


with open("setting.json", "r", encoding="utf8") as setup:
    setting = json.load(setup)


class CogExtension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cls = Classroom()
        self.is_send = DbQueue()
        self.is_send.load_data()
        self.anc_ch = int(setting['anc_channel'])
        self.hw_ch = int(setting['hw_channel'])
