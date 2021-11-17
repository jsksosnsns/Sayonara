import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from NaoRobot.events import register as MEMEK
from NaoRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/674bb34bc80e2a6aaa0b6.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  NAO = f"**Holla, I'm Akira Robot!** \n\n"
  NAO += "🔴 **I'm Working Properly** \n\n"
  NAO += "🔴 **My Master : [Tonic](https://t.me/Bukan_guudlooking)** \n\n"
  NAO += f"🔴 **Telethon Version : {tlhver}** \n\n"
  NAO += f"🔴 **Pyrogram Version : {pyrover}** \n\n"
  NAO += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Akiramanagerbot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/AkiraSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=NAO,  buttons=BUTTON)
