from discord import Embed
from .colors import *

async def about(message):
    embed = Embed(
        title = "EmmaBot",
        description = 
        "<a:arrowright:902959502989598830> **Developer:** Jackzy#0001\n<a:arrowright:902959502989598830> **Python:** 3.10.0\n<a:arrowright:902959502989598830> **Library:** [discord.py async](https://github.com/Rapptz/discord.py/)\n<a:arrowright:902959502989598830> **Invite me:** [here](https://discord.com/api/oauth2/authorize?client_id=869984249875427338&permissions=8&scope=bot)\n<a:arrowright:902959502989598830> **For devs: ** [source code](https://github.com/jackzyOS/ZorzBot)",
        color = pink)

    await message.channel.send(embed = embed)