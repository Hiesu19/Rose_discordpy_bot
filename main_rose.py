
import discord
from discord.ext import commands

from discord.ext import tasks
from itertools import cycle

import cogs.music
import cogs.thoitiet
import cogs.messenger

from dotenv.main import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")

cogs = [cogs.music, cogs.thoitiet, cogs.messenger]

client = commands.Bot(command_prefix='', intents=discord.Intents.all())
status = cycle(["Gone", "On the ground"])


@client.event
async def on_ready():
    print('Bot đang chạy !!!')
    print('We have logged in as {0.user}'.format(client))
    change_status.start()
    for item in cogs:
        await item.setup(client)


@tasks.loop(seconds=100)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


client.run(token)
