import discord, os
from .colors import *

async def disconnect(message):
    if str(message.author.id) in os.listdir("./data_base/cool_ppl"):
        if message.guild.me.guild_permissions.move_members:
            if len(message.mentions) != 0:
                await message.mentions[0].edit(voice_channel = None)
                embed = discord.Embed(
                    description = "Made sure that " + str(message.mentions[0]) + " is not in any VC!",
                    color = green)
                embed.set_author(
                    name = "Success",
                    icon_url = "https://media.discordapp.net/attachments/737046647476846673/825811629622951936/tick.png")

                await message.channel.send(embed = embed)
            else:
                embed = discord.Embed(
                    description = "Please mention a person!",
                    color = red)
                embed.set_author(
                    name = "Error",
                    icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")
                
                await message.channel.send(embed = embed)
        else:
            embed = discord.Embed(
                description = "Missing permissions: `move_members`",
                color = red)
            embed.set_author(
                name = "Error",
                icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")
            
            await message.channel.send(embed = embed)
    else:
        embed = discord.Embed(
            description = "You are not on the cool people list!",
            color = red)
        embed.set_author(
            name = "Error",
            icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")
        
        await message.channel.send(embed = embed)

async def random_disc(message):
    ...

        