from random import choice
from asyncio import sleep
import os
from .colors import *

activeServers = []

async def roulette(message):
	if message.guild.id in activeServers:
		await message.channel.send("A roulette is already running in this server. Please wait for it to end and then try again.")
	elif not str(message.author.id) in os.listdir("./data_base/cool_ppl"):
		await message.channel.send("You aren't cool enough to use this command!")
	else:
		tarca = choice([member for member in message.guild.members if message.guild.me.top_role.position>member.top_role.position and member.id != message.guild.owner_id])
		
		if message.guild.me.guild_permissions.ban_members:
			activeServers.append(message.guild.id)
			await message.channel.send("Srečnež, ki bo odfukan iz serverja je...")
			await sleep(5)
			await message.channel.send(":tada: " + tarca.mention + " :tada:")
			await message.channel.send("Maš 5 min. da se posloviš")
			await sleep(300)
			await tarca.send("https://discord.gg/an4gXVRrPz")
			await tarca.send("Če ne dela invite piši u DM: Jackzy#9999")
			await tarca.ban(reason="Unlucky")
			await message.channel.send("Banned " + tarca.mention)
			await message.channel.send("Unbanning in 2 mins...")
			await sleep(120)
			await tarca.unban()
			await message.channel.send("Unbanned " + str(tarca))
			activeServers.remove(message.guild.id)
		else:
			await message.channel.send("I need `ban members` permission!")





	
