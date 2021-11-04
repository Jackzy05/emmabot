from discord import Embed
import os
from .colors import *

async def setprefix(message):
	args = message.content.split()

	if message.author.guild_permissions.administrator:
		if len(args) == 1:
			embed = Embed(
				description = "1 argument is required but `0` were given",
				color = red)
			embed.set_author(
				name = "Error",
				icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

			await message.channel.send(embed = embed)
		elif len(args) != 2:
			embed = Embed(
				description = "At the moment prefixes can't include spaces!",
				color = red)
			embed.set_author(
				name = "Error",
				icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

			await message.channel.send(embed = embed)
		else:
			prefix = args[1]
			
			f = open("./data_base/prefixes/"+str(message.guild.id)+".txt", "w")
			f.write(prefix)
			f.close()

			embed = Embed(
				description = "Prefix has been set to " + "`" + prefix + "`", 
				color = green)
			embed.set_author(
				name = "Success", 
				icon_url="https://media.discordapp.net/attachments/737046647476846673/825811629622951936/tick.png")

			await message.channel.send(embed=embed)
	else:
		embed = Embed(
			description = "You are missing the following permission: `administrator`",
			color = red)
		embed.set_author(
			name = "Error",
			icon_url ="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

		await message.channel.send(embed = embed)

async def resetprefix(message):
	if message.author.guild_permissions.administrator:
		if not str(message.guild.id) + ".txt" in os.listdir("./data_base/prefixes/"):
			embed = Embed(
				description = "The bot is already using the default prefix!",
				color = red)
			embed.set_author(
				name = "Error",
				icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

			await message.channel.send(embed = embed)
		else:
			os.remove("./data_base/prefixes/"+str(message.guild.id)+".txt")
			f = open("./data_base/prefixes/default.txt", "r")
			default = f.read()
			f.close()
			
			embed = Embed(
				description = "Prefix has been reset to " + "`" + default + "`", 
				colour = green)
			embed.set_author(
				name="Success", 
				icon_url="https://media.discordapp.net/attachments/737046647476846673/825811629622951936/tick.png")

			await message.channel.send(embed = embed)
	else:
		embed = Embed(
			description = "You are missing the following permission: `adminsitrator`",
			color = red)
		embed.set_author(
			name = "Error",
			icon_url ="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

		await message.channel.send(embed = embed)

	