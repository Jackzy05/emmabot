import discord
from .colors import *

async def kick(message):
	args = message.content.split()

	if message.author.guild_permissions.kick_members:
		member = message.mentions[0]
		
		if len(message.mentions) != 1:
			embed = discord.Embed(
				description = "Please mention 1 person!",
				color = red)
			embed.set_author(
				name = "Error",
				icon_url="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")
					
			await message.channel.send(embed = embed)	
		elif message.author.id != member.id:
			if member.id != message.guild.owner_id:
				if message.guild.me.guild_permissions.kick_members and member.top_role.position < message.guild.me.top_role.position: 
					await member.kick()
					
					embed = discord.Embed(
						description = "Kicked " + str(member),
						color = green)
					embed.set_author(
						name = "Success",
						icon_url="https://media.discordapp.net/attachments/737046647476846673/825811629622951936/tick.png")
								
					await message.channel.send(embed = embed)
				else:
					embed = discord.Embed(
						description = "**Possible issues:** I am missing the `kick_members` permission or the person you are trying to kick has a higher role than me!",
						color = red)
					embed.set_author(
						name = "Error",
						icon_url="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")
					
					await message.channel.send(embed = embed)
			else:
				embed = discord.Embed(
					description = "No one can kick the server owner!",
					color = red)
				embed.set_author(
					name = "Error",
					icon_url="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")
				
				await message.channel.send(embed = embed)
		else:
			await message.channel.send("Just leave the server lol.")
	else:
		embed = discord.Embed(
			description = "Permission required: `kick_members`",
			color = red)
		embed.set_author(
			name = "Error",
			icon_url="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")
				
		await message.channel.send(embed = embed)

