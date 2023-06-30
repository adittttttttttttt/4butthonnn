# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from helper_func import encode


@Bot.on_message(
    filters.private
    & filters.user(ADMINS)
    & ~filters.command(
        ["start", "users", "broadcast", "ping", "uptime", "batch", "genlink"]
    )
)
async def channel_post(client: Client, message: Message):
Expand All
	@@ -32,10 +49,10 @@ async def channel_post(client: Client, message: Message):
            chat_id=client.db_channel.id, disable_notification=True
        )
    except Exception as e:
        print(e)
        await reply_text.edit_text("<b>Telah Terjadi Error...</b>")
        return
    converted_id = post_message.message_id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
Expand All
	@@ -57,18 +74,19 @@ async def channel_post(client: Client, message: Message):
    )

    if not DISABLE_CHANNEL_BUTTON:
        await post_message.edit_reply_markup(reply_markup)


@Bot.on_message(
    filters.channel & filters.incoming & filters.chat(CHANNEL_ID) & ~filters.edited
)
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = message.message_id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
Expand All
	@@ -83,5 +101,5 @@ async def new_post(client: Client, message: Message):
    )
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
