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
        self.history_msg_id = DbQueue()
        self.anc_ch = int(setting['anc_channel'])
        self.hw_ch = int(setting['hw_channel'])
