import discord

async def emoji(message):
    args = message.content.split()

    if len(args) == 1:
        pass
    else:
        if args[1].is_custom_emoji() and args[1].is_unicode_emoji():
            await message.channel.send("ffs")
        else:
            await message.channel.send("lol")