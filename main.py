import discord
import os
from commands import *
print("✓ Imports done")
	
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

f = open("token.txt", "r")
token = f.read()
f.close()

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers!"))
	print("✓ Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	if message.author.bot:
  		return
	
	if str(message.guild.id)+".txt" in os.listdir("./data_base/prefixes/"):
		f = open("./data_base/prefixes/"+str(message.guild.id)+".txt", "r")
		prefix = f.read()
		f.close()
		if len(message.mentions) != 0:
			if message.mentions[0].id == client.user.id:
				await message.channel.send("My prefix for this server is " + "`" + prefix + "`")
	else:
		f = open("./data_base/prefixes/default.txt", "r")
		prefix = f.read()
		f.close()
		if len(message.mentions) != 0:
			if message.mentions[0].id == client.user.id:
				await message.channel.send("My prefix for this server is " + "`" + prefix + "`")


	if message.content.startswith(prefix):
		args = message.content[len(prefix):]
		komanda = args.split(" ")
		if komanda[0] in commands:
			await commands[komanda[0]](message)
		else:
			embed = discord.Embed(
				description = "The " + "`" + komanda[0] + "`" + " command doesn't exist! Please use `e!help` to get a full list of commands!", 
				colour = red)
			embed.set_author(
				name="Error", 
				icon_url="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")

			await message.channel.send(embed=embed)

@client.event
async def on_member_join(member):
	f = open("./data_base/ping_on_joins/"+str(member.guild.id)+".txt", "r")
	channel_id = f.read()
	f.close()

	channel = client.get_channel(int(channel_id))
	await channel.send(f"{member.mention}")
	await channel.purge(limit = 1)

@client.event
async def on_message_edit(message_before, message_after):
	global editor, prej, potem
	editor = message_before.author.name
	
	prej = message_before.content
	potem = message_after.content

	edited_msgs[message_before.guild.id] = (prej, potem, editor)

edited_msgs = {}

async def neki():
	return edited_msgs

commands = {
	"ping-on-join": ping_on_join,
	"setprefix": setprefix,
	"juje": juje,
	"ping": ping,
	"help": help,
	"pfp": pfp,
	"nick": nick,
	"cnick": cnick,
	"ghostping": ghostping,
	"roulette": roulette,
	"kick": kick,
	"add": jaki_decki_add,
	"remove": jaki_decki_remove,
	"clear": clear,
	"ban": ban,
	"cool-person-add": add_cool_people,
	"cool-person-remove": remove_cool_people,
	"disable-ping-on-join": del_poj,
	"pp": pp,
	"resetprefix": resetprefix,
	"gayrate": gayrate,
	"8ball": ball,
	"invite": invite,
	"mute": mute,
	"unmute": unmute,
	"emma": emma,
	"emma-upload": emma_upload,
	"about": about,
	"disconnect": disconnect,
	"iq": iq,
	"emoji": emoji,
	"info": info,
	"editsnipe": editsnipe
}

client.run(token)