import discord
from discord.ext import commands
from cogs.mod.embed_mod import *

class messenger (commands.Cog):
    def __init__(self , client):
        self.client = client

    @commands.command()
    async def hello(self , ctx):
        hello_mes = messenger_enb("Hello {}, uwu !".format(ctx.author.name))
        await ctx.send(embed = hello_mes)

    @commands.command()
    async def ping(self , ctx) :
        ping_ = self.client.latency
        ping =  round(ping_ * 1000)
        ping_mes = messenger_enb("Pong {}ms !!!".format(ping))
        await ctx.send(embed = ping_mes)

    @commands.command()
    async def helpme(self , ctx):
        await ctx.send(embed = help_emb())

    @commands.command()
    async def xoa(ctx , amount = 1):
        await ctx.channel.purge(limit = amount+1)
        await ctx.message.delete()
        print("Rosé đã xóa {} dòng !" . format(amount))


async def setup(client):
    await client.add_cog(messenger(client))