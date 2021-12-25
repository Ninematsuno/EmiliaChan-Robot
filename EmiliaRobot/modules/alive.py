import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmiliaRobot.events import register
from EmiliaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/322db0b3880fb5ee0ee0c.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Emilia.** \n\n"
    TEXT += "❂ **I'm Working Properly** \n\n"
    TEXT += f"❂ **My Master : [ZenitsuID](https://t.me/ZenitsuID)** \n\n"
    TEXT += f"❂ **Library Version :** `{telever}` \n\n"
    TEXT += f"❂ **Telethon Version :** `{tlhver}` \n\n"
    TEXT += f"❂ **Pyrogram Version :** `{pyrover}` \n\n"
    TEXT += "**Thanks For Adding me Here**"
    BUTTON = [
        [
            Button.url("Help", "https://t.me/Emilia_xbot?start=help"),
            Button.url("Source Code​", "https://github.com/ZenitsuID/Emilia-Robot"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
