import discord
from discord.ext import commands
from cogs.mod.modun import *
import time
from cogs.mod.embed_mod import *

class thoitiet(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def thoitiet(self ,ctx):
		data = weather()	
		try:

			channel = discord.utils.get(ctx.guild.channels, name="thoi_tiet")
			channel_id = channel.id  
		except:
			
			guild = ctx.message.guild
			await guild.create_text_channel("thoi_tiet")    
			channel = discord.utils.get(ctx.guild.channels, name="thoi_tiet")
			channel_id = channel.id  
		kenh = self.client.get_channel(channel_id)
		await kenh.send(embed = weather_emb(data))


	@commands.command()
	async def forecast(self ,ctx , week = 5 ):
		data = forecast()
		week_str = str(week)
		#tao kenh
		try:

			channel = discord.utils.get(ctx.guild.channels, name="forecast")
			channel_id = channel.id  
		except:
			
			guild = ctx.message.guild
			await guild.create_text_channel("forecast")    
			channel = discord.utils.get(ctx.guild.channels, name="forecast")
			channel_id = channel.id

		
		if week_str.isdecimal():
			if week<= 12 and week >=1:		
				kenh = self.client.get_channel(channel_id)
				for i in range (0 , week):
					await kenh.send(embed = forecast_emb(data , i))
			else:
				await ctx.send( embed = messenger_enb("Tối đa 12 ngày thôi !"))
		else:
			await ctx.send( embed = messenger_enb("Sai cú pháp rồi !"))

async def setup(client):
	await client.add_cog(thoitiet(client))