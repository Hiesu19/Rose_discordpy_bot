await channel.send("Hai Bà Trưng, Hà Nội, Việt Nam")
		await channel.send( time.ctime(data['location']['localtime_epoch']))
		await channel.send("{}°C, {}".format(data['current']['temp_c'] ,dich(data['current']['condition']['text'])))
		await channel.send("Độ ẩm: {}%.".format(data['current']['humidity']))