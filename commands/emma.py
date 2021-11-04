from random import choice
import os
from discord import File, Embed
from .colors import *

async def emma(message):
	args = message.content.split()

	if len(args) != 1:
		embed = Embed(
			description = "0 arguments are required but `" + str(len(args) - 1) + "` were given!",
			color = red)
		embed.set_author(
			name = "Error",
			icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

		await message.channel.send(embed = embed)
	else:
		path = r"./data_base/pics/emma pics"

		random_filename = choice([
			x for x in os.listdir(path)
			if os.path.isfile(os.path.join(path, x))
		])

		file = File("./data_base/pics/emma pics/" + random_filename)
		
		embed = Embed(
			title = "Our angel :angel:",
			color = pink)
		embed.set_footer(
			text = "Requested by " + str(message.author),
			icon_url = message.author.avatar_url)
		embed.set_image(
			url = "attachment://" + random_filename)
		
		await message.channel.send(file = file, embed = embed)

async def emma_upload(message):
	if message.author.id == 399177749664628736:
		if len(message.attachments) != 1:
			embed = Embed(
				description = "**Possible issues:** You either didn't attach any files or you attached more than 1 file!",
				color = red)
			embed.set_author(
				name = "Error",
				icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

			await message.channel.send(embed = embed)
		else:
			f = open("./data_base/counter.txt", "r")
			num = f.read()
			
			f = open("./data_base/counter.txt", "w")
			f.write(str(int(num) + 1))
			
			f = open("./data_base/counter.txt", "r")
			file = f.read()
			f.close()
			
			await message.attachments[0].save("./data_base/pics/emma pics/emma" + file + ".png")

			embed = Embed(
				description = "Your picture was successfully added to the emma pics list!",
				color = green)
			embed.set_author(
				name = "Success",
				icon_url = "https://media.discordapp.net/attachments/737046647476846673/825811629622951936/tick.png")

			await message.channel.send(embed = embed)
	else:
		pass
