from discord import Embed
import os
from .colors import *

async def ping_on_join(message):
	args = message.content.split()
	
	if message.author.guild_permissions.administrator:
		if len(args) != 2:
			embed = Embed(
				description = "1 argument is required, but " + "`" + str(len(args[1:])) + "`" + " were given!",
				color = red)
			embed.set_author(
				name = "Error",
				icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")
				
			await message.channel.send(embed = embed)
		elif len(message.channel_mentions) != 1:
			embed = Embed(
				description = "Please mention a channel!",
				color = red)
			embed.set_author(
				name = "Error",
				icon_url="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")
				
			await message.channel.send(embed=embed)
		else:
			channel = str(message.channel_mentions[0].id)
			f = open("./data_base/ping_on_joins/"+str(message.guild.id)+".txt", "w")
			f.write(channel)
			f.close()

			embed = Embed(
				description = "New members will now be ghostpinged in " + "<#" + channel + "> when they join the server!" , 
				color = green)
			embed.set_author(
				name = "Success", 
				icon_url = "https://media.discordapp.net/attachments/737046647476846673/825811629622951936/tick.png")

			await message.channel.send(embed=embed)
	else:
		embed = Embed(
			description = "You are missing the following permission: `administrator`",
			color = red)
		embed.set_author(
			name = "Error",
			icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

		await message.channel.send(embed = embed)

async def del_poj(message):
	args = message.content.split()
	
	if message.author.guild_permissions.administrator:
		if len(args) != 1:
			embed = Embed(
				description = "0 arguments are required, but " + "`" + str(len(args[1:])) + "`" + " were given!",
				color = red)
			embed.set_author(
				name = "Error",
				icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")
				
			await message.channel.send(embed = embed)
		elif not str(message.guild.id)+".txt" in os.listdir("./data_base/ping_on_joins/"):
			embed = Embed(
				description = "Ping-on-join is already disabled!",
				color = red)
			embed.set_author(
				name = "Error",
				icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

			await message.channel.send(embed = embed)
		else:
			os.remove("./data_base/ping_on_joins/"+str(message.guild.id)+".txt")
			embed = Embed(
				description = "New members will no longer be ghostpinged!",
				color = green)
			embed.set_author(
				name = "Success",
				icon_url = "https://media.discordapp.net/attachments/737046647476846673/825811629622951936/tick.png")
				
			await message.channel.send(embed = embed)
	else:
		embed = Embed(
			description = "You are missing the following permission: `administrator`",
			color = red)
		embed.set_author(
			name = "Error",
			icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")
			
		await message.channel.send(embed = embed)

