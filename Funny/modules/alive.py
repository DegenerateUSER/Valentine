import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Funny.events import register as MEMEK
from Funny import telethn as tbot

PHOTO = "https://telegra.ph/file/22692f689fdf834b2ddad.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  YUMEKO = "**Holla I'm Himeno!** \n\n"
  YUMEKO += "×**I'm Working Properly** \n\n"
  YUMEKO += "×**My Owner : [Zeref](https://t.me/FringesBright)**× \n\n"
  YUMEKO += f"×**Telethon Version : {tlhver}** \n\n"
  YUMEKO += f"×**Pyrogram Version : {pyrover}** \n\n"
  YUMEKO += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/HimenoXBot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/Himenosupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=YUMEKO,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  YUMEKO = "✅ **bot restarted successfully**\n\n• Admin list has been **updated**"
  BUTTON = [[Button.url("📡 ᴜᴘᴅᴀᴛᴇs", "https://t.me/Himenosupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=YUMEKO,  buttons=BUTTON)
