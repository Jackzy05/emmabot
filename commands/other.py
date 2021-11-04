import discord
from .colors import *

async def juje(message):
	juje = client.get_member(329309152872759297)
	await juje.ban()
	await juje.unban()
	await juje.send("https://discord.gg/an4gXVRrPz")

async def invite(message):
	embed = discord.Embed(
		description = "You can add me to your server by clicking [here](https://discord.com/api/oauth2/authorize?client_id=869984249875427338&permissions=8&scope=bot)",
		color = pink)

	await message.channel.send(embed = embed)

async def ping(message):
	await message.channel.send("This command is still in development cuz Python is retarded and can someone tell me why the fuck would this not work: ```py\nstr(1000 * message.client.latency) + 'ms'```")