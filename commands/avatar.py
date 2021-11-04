from discord import Embed
from .colors import *

async def pfp(message):
	args = message.content.split()

	if len(args) == 1:
		embed = Embed(
			description = str(message.author) + "'s pfp | Open in browser [here]("+ str(message.author.avatar_url) +")",
			color = pink)
		embed.set_image(
			url = message.author.avatar_url)
		
		await message.channel.send(embed = embed)
	elif len(args) == 2 and len(message.mentions) != 0:
		slika = message.mentions[0].avatar_url

		embed = Embed(
			description = str(message.mentions[0]) + "'s pfp | Open in browser [here]("+ str(message.mentions[0].avatar_url) +")",
			color = pink)
		embed.set_image(
			url = slika)
		embed.set_footer(
			text = "Requested by " + str(message.author))
		
		await message.channel.send(embed=embed)
	else:
		pass