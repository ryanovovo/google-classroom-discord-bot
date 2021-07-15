import discord
from discord.ext import commands, tasks
import os
import json

with open("setting.json", "r", encoding="utf8") as jfile:
    setting = json.load(jfile)

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_ready():
    print("bot is online")


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

bot.run(setting['TOKEN'])

