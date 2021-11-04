import os
from discord import Embed
from .colors import *

async def add_cool_people(message):
    member = message.mentions[0].id
    
    if message.author.id != 399177749664628736:
        await message.channel.send("Only my lovely husband (jackzy) can use this command!")
        return
    elif len(message.mentions) == 0:
        return
    elif str(member) in os.listdir("./data_base/cool_ppl/"):
        await message.channel.send("This person is already on the cool people list!")
        return

    f = open("./data_base/cool_ppl/" + str(member), "w")
    f.close()

    embed = Embed(
        description = str(message.mentions[0].mention) + " has been added to the cool people list!",
        color = green)
    embed.set_author(
        name = "Success",
        icon_url = "https://media.discordapp.net/attachments/737046647476846673/825811629622951936/tick.png")
    
    await message.channel.send(embed = embed)

async def remove_cool_people(message):
    member = message.mentions[0].id
    
    if message.author.id != 399177749664628736:
        await message.channel.send("Only my lovely husband (jackzy) can use this command!")
        return
    elif len(message.mentions) == 0:
        return
    elif not str(member) in os.listdir("./data_base/cool_ppl/"):
        await message.channel.send("This person is not on the cool people list!")
        return

    os.remove("./data_base/cool_ppl/" + str(member))

    embed = Embed(
        description = str(message.mentions[0].mention) + " has been removed from the cool people list!",
        color = green)
    embed.set_author(
        name = "Success",
        icon_url = "https://media.discordapp.net/attachments/737046647476846673/825811629622951936/tick.png")
    
    await message.channel.send(embed = embed)