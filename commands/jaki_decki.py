from discord import Embed
from .colors import *

async def jaki_decki_add(message):
	member = message.mentions[0]
	guild = message.guild
	role = guild.get_role(768741348198187050)
	da_queenz = guild.get_role(828936593229611018)
	da_king = guild.get_role(841220882525454368)
    
	if len(message.mentions) == 0:
		await message.channel.send("Invalid member mention!")
		return
	elif message.guild.id != 751539503352512523:
		await message.channel.send("Can't use this command in this server!")
		return
	
	if da_queenz in message.author.roles or da_king in message.author.roles:
		if message.author.id != member.id:
			if member.id != message.guild.owner_id:
				if message.guild.me.guild_permissions.manage_roles and member.top_role.position<message.guild.me.top_role.position: 
					await member.add_roles(role)
					embed = Embed(
						description = "Successfully added " + member.mention + " the " + role.mention + " role!", 
						colour = green)
					embed.set_author(
						name="Success", 
						icon_url="https://media.discordapp.net/attachments/737046647476846673/825811629622951936/tick.png")
					embed.set_footer(
						text="We <3 Emma Watson", 
						icon_url="https://cdn.discordapp.com/attachments/751533557687779439/871110688028893254/Jackzypng.png")

					await message.channel.send(embed=embed)
				else:
					embed = Embed(
						description = "I don't have sufficient permissions!",
						color = red
						)
					embed.set_author(
						name = "Error",
						icon_url="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png"
						)
			else:
				embed = Embed(
					description = "I cant't give roles to the server owner!",
					color = red
					)
				embed.set_author(
					name = "Error",
					icon_url="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png"
					)
		else:
			await message.channel.send("You can't give the role to yourself nigga.")
			return
	else:
		await message.channel.send("You are not a part of the Jaki Dečki council!")
		return

async def jaki_decki_remove(message):
	member = message.mentions[0]
	guild = message.guild
	role = guild.get_role(768741348198187050)
	da_queenz = guild.get_role(828936593229611018)
	da_king = guild.get_role(841220882525454368)

	if message.guild.id != 751539503352512523:
		await message.channel.send("Can't use this command in this server!")
		return
    
	if da_queenz in message.author.roles or da_king in message.author.roles:
		if message.author.id != member.id:
			if member.id != message.guild.owner_id:
				if message.guild.me.guild_permissions.manage_roles and member.top_role.position<message.guild.me.top_role.position: 
					await member.remove_roles(role)
					embed = Embed(
						description = "Successfully removed " + member.mention + " the " + role.mention + " role!",
						colour = green)
					embed.set_author(
						name="Success", 
						icon_url="https://media.discordapp.net/attachments/737046647476846673/825811629622951936/tick.png")
					embed.set_footer(
						text="We <3 Emma Watson", 
						icon_url="https://cdn.discordapp.com/attachments/751533557687779439/871110688028893254/Jackzypng.png")

					await message.channel.send(embed=embed)
				else:
					embed = Embed(
						description = "I don't have sufficient permissions!",
						color = red
						)
					embed.set_author(
						name = "Error",
						icon_url="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png"
						)
			else:
				embed = Embed(
					description = "I cant't give roles to the server owner!",
					color = red
					)
				embed.set_author(
					name = "Error",
					icon_url="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png"
					)
		else:
			await message.channel.send("You can't give the role to yourself nigga.")
			return
	else:
		await message.channel.send("You are not a part of the Jaki Dečki council!")
		return

