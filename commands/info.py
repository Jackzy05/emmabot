import discord
from .colors import *
import time

async def info(message):
    args = message.content.split()
    
    if len(message.mentions) == 0:
        rolelist = [r.mention for r in message.author.roles if r != message.guild.default_role]
        roles = ", ".join(rolelist)
        embed = discord.Embed(
            title = "Member info for " + str(message.author),
            description = message.author.mention,
            color = pink)
        embed.set_thumbnail(url = message.author.avatar_url)
        embed.add_field(
            name = "Created at:",
            value = "<t:"+str(int(time.mktime(message.author.created_at.timetuple())))+":f>\n" + "<t:"+str(int(time.mktime(message.author.joined_at.timetuple())))+":R>")
        embed.add_field(
            name = "Joined at:",
            value = "<t:"+str(int(time.mktime(message.author.joined_at.timetuple())))+":f>\n" + "<t:"+str(int(time.mktime(message.author.joined_at.timetuple())))+":R>",
            inline = False)
        embed.add_field(
            name = "Roles " + "(" + str(len(rolelist)) + ")",
            value = roles)
        embed.add_field(
            name = "Badges:",
            value = str(message.author.public_flags),
            inline = False)
        embed.set_footer(text = "User ID: " + str(message.author.id))

        await message.channel.send(embed = embed)
    else:
        rolelist = [r.mention for r in message.mentions[0].roles if r != message.guild.default_role]
        roles = ", ".join(rolelist)
        embed = discord.Embed(
            title = "Member info for " + str(message.mentions[0]),
            description = message.mentions[0].mention,
            color = pink)
        embed.set_thumbnail(url = message.mentions[0].avatar_url)
        embed.add_field(
            name = "Created at:",
            value = "<t:"+str(int(time.mktime(message.mentions[0].created_at.timetuple())))+":f>\n" + "<t:"+str(int(time.mktime(message.author.joined_at.timetuple())))+":R>")
        embed.add_field(
            name = "Joined at:",
            value = "<t:"+str(int(time.mktime(message.mentions[0].joined_at.timetuple())))+":f>\n" + "<t:"+str(int(time.mktime(message.author.joined_at.timetuple())))+":R>",
            inline = False)
        embed.add_field(
            name = "Roles " + "(" + str(len(rolelist)) + ")",
            value = roles)
        embed.add_field(
            name = "Badges:",
            value = str(message.mentions[0].public_flags),
            inline = False)
        embed.set_footer(text = "User ID: " + str(message.mentions[0].id))

        await message.channel.send(embed = embed)

