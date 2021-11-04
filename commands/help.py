from discord import Embed
from .colors import *

async def help(message):
	args = message.content.split()
	
	if len(args) == 1:
		embed = Embed( 
			title = "EmmaBot's help page",
			url = "https://github.com/jackzyOS/ZorzBot",
			description = "EmmaBot is an open source discord bot with a theme of Emma Watson <a:rainbowheart:901863328975044639>", 
			color = pink)
		embed.add_field(
			name = "Mod/Admin", 
			value = "`ban`, `clear`, `cnick`, `disable-ping-on-join`, `kick`, `mute`, `mute-repair`, `mute-setup`, `ping-on-join`, `resetprefix`, `setprefix`, `unmute`", 
			inline = False)
		embed.add_field(
			name = "General", 
			value = "`about`, `editsnipe`, `emma`, `emoji`, `help`, `info`, `invite`, `nick`, `pfp`, `ping`",
			inline = False)
		embed.add_field(
			name = "Fun", 
			value = "`8ball`, `gayrate`, `iq`, `math`, `mathboard`, `pp`", 
			inline = False)
		embed.add_field(
			name = "Cool People", 
			value = "`ghostping`, `roulette`, `disconnect`, `random-disc`",
			inline = False)
		embed.add_field(
			name = "Jaki dečki council", 
			value = "`add`, `remove`",
			inline = False)
		embed.add_field(
			name = "Dev", 
			value = "`cool-person-add`, `cool-person-remove`, `emma-upload`",
			inline = False)
		embed.set_footer(
			text="Requested by " + str(message.author) + " | Use e!help <command> for more info on a command.",
			icon_url = message.author.avatar_url)
		embed.set_thumbnail(
			url = "https://pbs.twimg.com/profile_images/1090425963/Emma_Twitt.png")

		await message.channel.send(embed=embed)
		return
	elif len(args) != 2:
		return
	
	match args[1]:
		case "ping-on-join":
			embed = Embed(
				description = "This command is very useful when you want to bring new member's attention to a specific channel.",
				color = pink)
			embed.set_author(
				name = "Mod/Admin > ping-on-join")
			embed.add_field(
				name = "Usage",
				value = "```e!ping-on-join <#channel>```")

			await message.channel.send(embed=embed)
		case "setprefix":
			embed = Embed(
				description = "This command allows you to change bot's prefix - the symbol/message you must type before any command.",
				color = pink)
			embed.set_author(
				name = "Mod/Admin > setprefix")
			embed.add_field(
				name = "Usage",
				value = "```e!setprefix <prefix>```")

			await message.channel.send(embed=embed)
		case "cnick":
			embed = Embed(
				description = "This command allows you to change members nicknames.",
				color = pink)
			embed.set_author(
				name = "Mod/Admin > Change nickname")
			embed.add_field(
				name = "Usage",
				value = "```e!cnick <@user> <new_nickname>```")

			await message.channel.send(embed=embed)
		case "kick":
			embed = Embed(
				description = "A quick way to remove(kick) a member from your server.",
				color = pink)
			embed.set_author(
				name = "Mod/Admin > Kick")
			embed.add_field(
				name = "Usage",
				value = "```e!kick <@user>```")

			await message.channel.send(embed=embed)
		case "ban":
			embed = Embed(
				description = "Permanently ban someone from your server!",
				color = pink)
			embed.set_author(
				name = "Mod/Admin > Ban")
			embed.add_field(
				name = "Usage",
				value = "```e!ban <@user>```")

			await message.channel.send(embed=embed)
		case "mute":
			embed = Embed(
				description = "Take a member's permission to speak in your server.",
				color = pink)
			embed.set_author(
				name = "Mod/Admin > Mute")
			embed.add_field(
				name = "Usage",
				value = "```e!mute <@user>```")

			await message.channel.send(embed=embed)
		case "clear":
			embed = Embed(
				description = "Delete up to 75 messages with one command!",
				color = pink)
			embed.set_author(
				name = "Mod/Admin > Clear")
			embed.add_field(
				name = "Usage",
				value = "```e!clear <num>```")

			await message.channel.send(embed=embed)
		case "nick":
			embed = Embed(
				description = "A quick way to change your own nickname.",
				color = pink)
			embed.set_author(
				name = "General > Nickname")
			embed.add_field(
				name = "Usage",
				value = "```e!nick <new_nickname>```")

			await message.channel.send(embed=embed)
		case "pfp":
			embed = Embed(
				description = "Get a direct link to the mentioned user's profile picture.",
				color = pink)
			embed.set_author(
				name = "General > Profile Picture")
			embed.add_field(
				name = "Usage",
				value = "```e!pfp <@user>```")

			await message.channel.send(embed=embed)
		case "ping":
			embed = Embed(
				description = "Check the bot's latency if for some reason you wanna know it lol.",
				color = pink)
			embed.set_author(
				name = "General > Ping")
			embed.add_field(
				name = "Usage",
				value = "```e!ping```")

			await message.channel.send(embed=embed)
		case "about":
			embed = Embed(
				description = "Get some extra information about this bot including it's source code.",
				color = pink)
			embed.set_author(
				name = "General > About")
			embed.add_field(
				name = "Usage",
				value = "```e!about```")

			await message.channel.send(embed=embed)
		case "roulette":
			embed = Embed(
				description = "Let yourself be surprised ;)",
				color = pink)
			embed.set_author(
				name = "Cool People > Russian Roulette")
			embed.add_field(
				name = "Usage",
				value = "```e!roulette```")

			await message.channel.send(embed=embed)

		case "add":
			embed = Embed(
				description = "Jaki Dečki council's stuff...",
				color = pink)
			embed.set_author(
				name = "Cool People > Jaki Dečki add")
			embed.add_field(
				name = "Usage",
				value = "```e!add <@user>```")

			await message.channel.send(embed=embed)
		case "remove":
			embed = Embed(
				description = "Jaki Dečki council's stuff...",
				color = 0xff9999)
			embed.set_author(
				name = "Cool People > Jaki Dečki remove")
			embed.add_field(
				name = "Usage",
				value = "```e!remove <@user>```")

			await message.channel.send(embed=embed)
		case _:
			embed = Embed(
				description = "The " + "`" + args[1] + "`" + " help command doesn't exist! Use `e!help` to see the full list of commands!", 
				colour = pink)
			embed.set_author(
				name="Error", 
				icon_url="https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")
			embed.set_footer(
				text="Requested by " + str(message.author), 
				icon_url=message.author.avatar_url)

			await message.channel.send(embed=embed)
		


