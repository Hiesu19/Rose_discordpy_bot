import discord
from discord.ext import commands
import youtube_dl
from discord import FFmpegPCMAudio
from cogs.mod.modun import *
from cogs.mod.embed_mod import *

class music(commands.Cog):
	def __init__(self, client):
		self.client = client

	def doc_file_mp3(self ,ctx,url):
		self.voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
		self.source = FFmpegPCMAudio(url)
		self.player = self.voice.play(self.source)


	@commands.command()
	async def join(self, ctx):
		if ctx.author.voice:	
			voice_channel = ctx.message.author.voice.channel
			await voice_channel.connect()
		
		else:
			await ctx.send(embed = messenger_enb("Không thấy ai ở trong phòng cả."))

	@commands.command()
	async def disconnect(self, ctx):
		if ctx.voice_client:
			await ctx.guild.voice_client.disconnect()
		else:
			await ctx.send(embed = messenger_enb("Em có ở trong đâu mà thoát."))

	@commands.command()
	async def play(self, ctx ,*, u = "Vivalavida Rose"):
		ctx.voice_client.stop()
		url = search_url(u)
		await ctx.send(embed = youtube_enb(url))
		FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
		YDL_OPTIONS = {'format':'bestaudio'}
		vc = ctx.voice_client
		with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
			info = ydl.extract_info(url, download = False)
			url2 = info['formats'][0]['url']
			source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)


			# source = discord.FFmpegAudio(opusaudio, executable='C:/Code/Python/Bot Discord/Rose/Rose_bot/ffmpeg')
			print("Rosé đang phát nhạc trên Youtube !")
			vc.play(source)


	@commands.command()
	async def pause(self, ctx ):
		voice_client = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
		if voice_client.is_playing():
			await ctx.voice_client.pause()
		else:
			await ctx.send(embed = messenger_enb("Hiện đang không phát bài nào."))	
		
	@commands.command()
	async def resume(self, ctx):
		voice_client = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
		if voice_client.is_paused():
			await ctx.voice_client.resume()
		else:
			await ctx.send(embed = messenger_enb("Em đang hát mà."))

	@commands.command()
	async def stop(self, ctx):
		ctx.voice_client.stop()
		await ctx.send(embed = messenger_enb("STOPED !"))

async def setup(client):
	await client.add_cog(music(client))