from random import randint
from random import choice
from discord import Embed
from .colors import *

async def pp(message): 
    args = message.content.split()

    num = randint(1, 7)
    length = ""

    for i in range(num):
        length += "="
         
    if len(args) == 1:
        embed = Embed(
            title = "Your PP:",
            description = "8" + length + "Đ",
            color = pink)
        
        await message.channel.send(embed = embed)
    elif len(message.mentions) == 0:
        embed = Embed(
            title = " ".join(args[1:]) + "'s PP:",
            description = "8" + length + "Đ",
            color = pink)
        
        await message.channel.send(embed = embed)
    else:
        embed = Embed(
            title = str(message.mentions[0]) + "'s PP:",
            description = "8" + length + "Đ",
            color = pink)
        
        await message.channel.send(embed = embed)

async def gayrate(message):
    args = message.content.split()
    num = randint(0, 100)
    gayrate = str(num) + "%"

    if len(args) == 1:
        embed = Embed(
        title = "Gayrate machine",
        description = "You are " + gayrate + " gay!",
        color = pink)
        embed.set_thumbnail(url = "https://d7hftxdivxxvm.cloudfront.net/?resize_to=width&src=https%3A%2F%2Fartsy-media-uploads.s3.amazonaws.com%2Fpj3o231MA6ygMyYxAOT_EQ%252F1024px-Rainbow_flag_breeze%2Bcopy.jpg&width=1200&quality=80")
    
        await message.channel.send(embed = embed)
    elif len(message.mentions) == 0:
        embed = Embed(
        title = "Gayrate machine",
        description = " ".join(args[1:]) + " is " + gayrate + " gay!",
        color = pink)

        embed.set_thumbnail(url = "https://d7hftxdivxxvm.cloudfront.net/?resize_to=width&src=https%3A%2F%2Fartsy-media-uploads.s3.amazonaws.com%2Fpj3o231MA6ygMyYxAOT_EQ%252F1024px-Rainbow_flag_breeze%2Bcopy.jpg&width=1200&quality=80")
    
        await message.channel.send(embed = embed)
    else:
        embed = Embed(
        title = "Gayrate machine",
        description = str(message.mentions[0]) + " is " + gayrate + " gay!",
        color = pink)

        embed.set_thumbnail(url = "https://d7hftxdivxxvm.cloudfront.net/?resize_to=width&src=https%3A%2F%2Fartsy-media-uploads.s3.amazonaws.com%2Fpj3o231MA6ygMyYxAOT_EQ%252F1024px-Rainbow_flag_breeze%2Bcopy.jpg&width=1200&quality=80")
    
        await message.channel.send(embed = embed)

async def ball(message):
    yes = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.", 
    "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes."]
    mid = ["Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again."]
    no = ["Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

    random = choice([True, False, "mid"])
    args = message.content.split()

    if len(args) == 1:
        embed = Embed(
            description = "1 argument is required!",
            color = red)
        embed.set_author(
            name = "Error",
            icon_url = "https://media.discordapp.net/attachments/737046647476846673/825812580912201748/cancel.png")
        
        await message.channel.send(embed = embed)
        return
    elif random == True:
        sentence = choice(yes)
        embed = Embed(
            title = ":8ball: The magic 8ball says:",
            description = ":white_check_mark: " + sentence,
            color = green)
    elif random == False:
        sentence = choice(no)
        embed = Embed(
            title = ":8ball: The magic 8ball says:",
            description = ":anger: " + sentence,
            color = red)
    else:
        sentence = choice(mid)
        embed = Embed(
            title = ":8ball: The magic 8ball says:",
            description = ":grey_question: " + sentence,
            color = 0xffe800)

    await message.channel.send(embed = embed)

async def iq(message):
    args = message.content.split()
    iq = randint(0, 200)

    if len(args) == 1:
        if message.mentions[0].id == 315446934502506497:
            embed = Embed(
                description = "Your IQ is 200 :nerd_face:",
                color = pink)
            embed.set_author(
                name = "IQ machine")
        else: 
            embed = Embed(
                description = "Your IQ is " + iq + " :nerd_face:",
                color = pink)
            embed.set_author(
                name = "IQ machine")

        await message.channel.send(embed = embed)
    elif len(message.mentions) == 0:
        embed = Embed(
            description = " ".join(args[1:]) + "'s IQ is " + str(iq) + " :nerd_face:",
            color = pink)
        embed.set_author(
            name = "IQ machine")

        await message.channel.send(embed = embed)
    else:
        embed = Embed(
            description = str(message.mentions[0]) + "'s IQ is " + str(iq) + " :nerd_face:",
            color = pink)
        embed.set_author(
            name = "IQ machine")

        await message.channel.send(embed = embed)

    




