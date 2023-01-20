import discord
from discord.ext import commands
from cogs.mod.modun import *
from cogs.mod.embed_mod import *


class chatGPT(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def chat(self, ctx ,*, ques = "Rosé là ai?"):
		data = search_gpt(ques)
		await ctx.send(embed = search_emb(ques , data))
		 

async def setup(client):
	await client.add_cog(chatGPT(client))