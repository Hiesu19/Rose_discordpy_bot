import discord
from discord.ext import commands
from pytube import YouTube
import time
from cogs.mod.modun import *


def messenger_enb(mess):
    embed = discord.Embed(
		title = mess, 
		colour = 0xff66ff , 
	)
    return embed

def youtube_enb(url):
    yt = YouTube(url)
    title = "Đang phát: " + yt.title
    time = "{} phút, {} giây." .format(int(yt.length/60) , int(yt.length)%60)
    views = yt.views
    thumbnail = yt.thumbnail_url
    embed = discord.Embed(
			title = title, 
			colour = 0xff66ff,
            url=url, 
		)
    embed.add_field(name = "Thời lượng:" , value = time , inline = False)
    embed.add_field(name = "Lượt xem:" , value = str(views)  , inline = True)
    embed.set_image(url = thumbnail)
    return embed

def weather_emb(data):
    icon_url = "https:"+data['current']['condition']['icon']
    icon_url = icon_url.replace("64x64", "128x128")

    embed = discord.Embed(
			title = "{}°C, {}\nĐộ ẩm {}%".format(data['current']['temp_c'] ,dich(data['current']['condition']['text']) , data['current']['humidity']), 
			colour = 0xff66ff , 
		)
    embed.set_thumbnail(url = icon_url)
    embed.add_field(name =  "Hai Bà Trưng, Hà Nội, Viêt Nam."  ,value =time.ctime(data['location']['localtime_epoch'] + 36000 ), inline=True)
    return embed

def forecast_emb(data , i):
    icon_url = "https://developer.foreca.com/static/images/symbols/" + data['forecast'][i]['symbol'] + ".png"
    thoitiet = dich( data['forecast'][i]['symbolPhrase'])
    thoigian = time.ctime(data['forecast'][i]['sunriseEpoch'] + 36000)
    thoigian = thoigian[0:-13]
    embed = discord.Embed(
			title = "{}.\n{}° / {}°" . format(thoigian ,  data['forecast'][i]['maxTemp'] , data['forecast'][i]['minTemp'] ,  )  ,
			colour = 0xff66ff , 
		)
    embed.set_thumbnail(url = icon_url)
    embed.add_field(name =  "Hai Bà Trưng, Hà Nội, Viêt Nam."  ,value = thoitiet, inline=True)
    return embed

def help_emb():
    embed = discord.Embed(
			title = "Help Rosé bot command ?",
			colour = 0xff66ff , 
		)
    embed.set_thumbnail(url = 'https://discord.bots.gg/img/logo_transparent_coloured.png')
    embed.add_field(name =  "join"  ,value = "Tham gia phòng thoại", inline=True)
    embed.add_field(name =  "disconnect"  ,value = "Ngắt kết nối phòng thoại", inline=True)
    embed.add_field(name =  "play + 'valume'"  ,value = "Phát bài hát trên Youtube (Mặc định Vivalavida của Rose)", inline=True)
    embed.add_field(name =  "pause/resume"  ,value = "Tạm dừng hát/Tiếp tục hát", inline=True)
    embed.add_field(name =  "chat"  ,value = "Trò chuyện trực tiếp với Rosé !", inline=True)
    embed.add_field(name =  "stop"  ,value = "Dừng hát", inline=True)
    embed.add_field(name =  "thoitiet"  ,value = "Xem thời tiết hiện tại (Mặc định Hai Bà Trưng, Hà Nội)", inline=True)
    embed.add_field(name =  "forecast + 'valume' " ,value = "Dự báo thời tiết (Mặc định 5 ngày, có thể thay đổi nhưng tối đa 12 ngày)", inline=True)
    embed.add_field(name =  "Một vài lệnh khác" ,value = "hello , ping ", inline=True)
    return embed    

def search_emb(ques , data):
    embed = discord.Embed(
			title = "#" + ques,
			colour = 0xff66ff , 
		)
    embed.add_field(name =  'Rosé:' ,value = data, inline=True)   
    return embed