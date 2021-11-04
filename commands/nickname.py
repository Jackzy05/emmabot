from discord import Embed
from .colors import *

async def nick(message):
	args = message.content.split()
	nick = message.content.split()[1:]
	
	args2 = str(message.author).split("#")
	old_nick = args2[:1]

	if len(nick) > 32:
		embed = Embed(
			description = "Nicknames can't be longer than 32 characters!",
			color = red)
		embed.set_author(
			name = "Error",
			icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

		await message.channel.send(embed = embed)
		return
	elif message.author.id != message.guild.owner_id:
		if message.guild.me.guild_permissions.manage_nicknames and message.author.top_role.position < message.guild.me.top_role.position:
			await message.author.edit(nick=" ".join(nick)) 
			embed = Embed(
				description = "Changed " + "`" + str(message.author) + "`" + "'s nickname from " + '"' + " ".join(old_nick) + '"' + " to " + '"' + " ".join(nick) + '"',
				color = green)
			embed.set_author(
				name = "Success",
				icon_url = "https://media.discordapp.net/attachments/737046647476846673/825811629622951936/tick.png")

			await message.channel.send(embed = embed)
		else:
			embed = Embed(
				description = "**Possible issues:** I am missing the `manage_nicknames` permission or you have a higer role than me.",
				color = red)
			embed.set_author(
				name = "Error",
				icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

			await message.channel.send(embed = embed)
	else:
		embed = Embed(
			description = "No one can change server owner's nickname!",
			color = red)
		embed.set_author(
			name = "Error",
			icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

		await message.channel.send(embed = embed)

async def cnick(message):
	args = message.content.split()
	args_num = len(args) - 1

	if message.author.guild_permissions.manage_nicknames:	
		if len(args) != 3:
			embed = Embed(
				description = "2 arguments are required but " + "`" + str(args_num) + "`" + " were given!",
				color = red)
			embed.set_author(
				name = "Error",
				icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

			await message.channel.send(embed = embed)
			return
		elif len(message.mentions) != 1:
			embed = Embed(
				description = "Please mention a person!",
				color = red)
			embed.set_author(
				name = "Error",
				icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

			await message.channel.send(embed = embed)
		elif len(" ".join(args[2:])) > 32:
			embed = Embed(
				description = "Nicknames cannot be longer than 32 characters!",
				color = red)
			embed.set_author(
				name = "Error",
				icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

			await message.channel.send(embed = embed)
			return

		member = message.mentions[0]
	
		if message.author.id != member.id:
			if member.id != message.guild.owner_id:
				if message.guild.me.guild_permissions.manage_nicknames and member.top_role.position<message.guild.me.top_role.position: 
					await member.edit(nick=" ".join(args[2:]))
					embed = Embed(
						description = "Changed " + "`" + str(message.mentions[0]) + "`" + "'s nickname to " + '"' + " ".join(args[2:]) + '"',
						color = green)
					embed.set_author(
						name = "Success",
						icon_url = "https://media.discordapp.net/attachments/737046647476846673/825811629622951936/tick.png")

					await message.channel.send(embed = embed)
				else:
					embed = Embed(
						description = "**Possible issues:** I am missing the `manage_nicknames` permission or the person who's nickname you are trying to change has a higher role than me.",
						color = red)
					embed.set_author(
						name = "Error",
						icon_url="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

					await message.channel.send(embed = embed)
			else:
				embed = Embed(
					description = "I cant't change owner's nickname!",
					color = red
					)
				embed.set_author(
					name = "Error",
					icon_url="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

				await message.channel.send(embed = embed)
		else:
			await message.channel.send("To change your own nickname use the `p!nick <nick>` command.")
	else:
		embed = Embed(
			description = "Permission required: `manage_nicknames`",
			color = red)
		embed.set_author(
			name = "Error",
			icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

		await message.channel.send(embed = embed)