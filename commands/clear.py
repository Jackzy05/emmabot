from asyncio import sleep
from .colors import *
from discord import Embed

async def clear(message):
	args = message.content.split()
	
	if message.author.guild_permissions.manage_messages:
		if message.guild.me.guild_permissions.manage_messages:
			if len(args) != 2:
				embed = Embed(
					description = "1 argument is required but " + "`" + str(len(args) - 1) + "`" + " were given!",
					color = red)
				embed.set_author(
					name = "Error",
					icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")
				
				await message.channel.send(embed = embed)
			elif not args[1].isnumeric():
				embed = Embed(
					description = "Please specify a number of how many messages should I clear!",
					color = red)
				embed.set_author(
					name = "Error",
					icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

				await message.channel.send(embed = embed)
			else:
				await message.channel.purge(limit = int(args[1]) + 1)
				await message.channel.send("Cleared " + "`"  + args[1] + "`" + " messages!")
				
				await sleep(2.5)
				await message.channel.purge(limit = 1)
		else:
			embed = Embed(
				description = "Missing permissions: `manage_messages`",
				color = red)
			embed.set_author(
				name = "Error",
				icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

			await message.channel.send(embed = embed)
	else:
		embed = Embed(
			description = "You are missing the following permissions: `manage_messages`",
			color = red)
		embed.set_author(
			name = "Error",
			icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

		await message.channel.send(embed = embed)





