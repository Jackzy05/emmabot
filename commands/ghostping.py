from discord import Embed
import os
from .colors import *

async def ghostping(message):
	args = message.content.split()
	št_pingov = int(args[2])
	tarča = args[1]

	if not str(message.author.id) in os.listdir("./data_base/cool_ppl"):
		await message.channel.send("You aren't cool enough to use this command!")
		return
	elif len(args) != 3:
		embed = Embed(
			description = "Invalid command format!",
			color = red
			)
		embed.set_author(
			name = "Error",
			icon_url="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png"
			)
		embed.add_field(
			name = "Usage",
			value = "```p!p <@user> <number>```"
			)

		await message.channel.send(embed=embed)
		return
	elif not args[2].isnumeric():
		embed = Embed(
			description = "Invalid number value. Didn't they teach you what numbers are? Well let me help you: https://en.wikipedia.org/wiki/Number",
			color = red
			)
		embed.set_author(
			name = "Error",
			icon_url="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png"
			)
		embed.add_field(
			name = "Usage",
			value = "```p!p <@user> <number>```"
			)

		await message.channel.send(embed=embed)
		return
	elif args[2] == "0":
		await message.channel.send("Can't ping someone 0 times!")
	elif št_pingov > 20:
		embed = Embed(
			description = "Pay me if you want more than 20 pings -> https://paypal.me/jackzy05",
			color = red
			)
		embed.set_author(
			name = "Error",
			icon_url="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png"
			)
		embed.add_field(
			name = "Usage",
			value = "```p!p <@user> <number>```"
			)

		await message.channel.send(embed=embed)
		return
	elif len(message.mentions) != 1:
		embed = Embed(
			description = "`" + args[1] + "` is not an user you moron. Ping an user like a man does!",
			color = red
			)
		embed.set_author(
			name = "Error",
			icon_url="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png"
			)
		embed.add_field(
			name = "Usage",
			value = "```p!p <@user> <number>```"
			)

		await message.channel.send(embed=embed)
		return
	
	await message.channel.purge(limit = 1)

	for i in range(št_pingov):
		await message.channel.send(tarča)
		
	await message.channel.purge(limit = št_pingov)