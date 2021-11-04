from .colors import *
from discord import Embed

async def editsnipe(message):
	embed = Embed(
		title = "Edit by " + editor,
		description = prej + " -> " + potem,
		color = pink)
		
	await message.channel.send(embed = embed)
    