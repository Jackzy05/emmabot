async def mute(message):
	if message.author.guild_permissions.administrator:
		if message.guild.me.guild_permissions.ban_members:
			
	await message.channel.send("<a:loading:902873820153651230> The `mute` command is still in develpoment. Thank you for your patience!")

async def unmute(message):
	await message.channel.send("<a:loading:902873820153651230> The `unmute` command is still in develpoment. Thank you for your patience!")