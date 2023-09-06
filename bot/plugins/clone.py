#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import asyncio

from typing import Union

from pyropatch.listen.message import Client as PClient

from pyrogram import Client, filters, enums
from pyrogram.types import Message

from bot import Config
from bot.bot import Bot


@Client.on_message(filters.command("clone") & filters.user(Config.AUTH_USERS) & filters.private)
async def clone(bot: Union[Bot, PClient], update: Message):
    
    target_title = (await bot.get_chat(Config.TARGET_CHANNEL)).title
    destination_title = (await bot.get_chat(Config.DESTINATION_CHANNEL)).title


    req_msg = await update.reply(f"Forward me the first msg from <b>{target_title}</b> or use <code>/skip</code> to copy from the start!")
    msg = await bot.listen_message(
        update.chat.id,
        filters=(
            filters.chat(update.chat.id) 
            & filters.user(update.from_user.id) & 
            (
                filters.forwarded & filters.text | 
                filters.regex(r"(https:\/\/t\.me\/(?:[A-Za-z0-9_]+\/?\d+|c\/\d+\/\d+))") |
                filters.command("skip")
            )
        )
    )
    await req_msg.delete()
    first_id = msg.forward_from_message_id if msg.forward_from else (0 if msg.text == "/skip" else int(msg.text.split("/")[-1]))
    
    
    req_msg = await update.reply(f"Forward me the last msg or send me the last msg link from <b>{target_title}</b>")
    msg = await bot.listen_message(
        update.chat.id,
        filters=(
            filters.chat(update.chat.id) 
            & filters.user(update.from_user.id) & 
            (filters.forwarded & filters.text | filters.regex(r"(https:\/\/t\.me\/(?:[A-Za-z0-9_]+\/?\d+|c\/\d+\/\d+))"))
        )
    )
    await req_msg.delete()
    last_id = msg.forward_from_message_id if msg.forward_from else int(msg.text.split("/")[-1])
    
    f = await update.reply(f"Copying Messages from <b>{target_title}</b> to <b>{destination_title}</b>")
    count = 0
    await asyncio.sleep(1)
    await f.edit("Copying...")
    async for msg in bot.iter_messages(Config.TARGET_CHANNEL, last_id, first_id):
        msg: Message
        if not msg.text:
            continue
        await bot.send_message(
            Config.DESTINATION_CHANNEL,
            text=msg.text.html,
            parse_mode=enums.ParseMode.HTML
        )
        if count %20 == 0:
            await f.edit(f"Copied: {count}\nRemaining: {last_id-msg.id}")
            await asyncio.sleep(5)
        count += 1
        await asyncio.sleep(0.2)
        
    await f.delete()


    await f.reply(f"Sucessfully copied {last_id} messages to <b>{destination_title}</b>")
    

