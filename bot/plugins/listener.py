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


@Client.on_message(filters.chat(Config.TARGET_CHANNEL) & filters.text, -2)
async def msg_listener(bot: Union[Bot, PClient], update: Message):

    if not update.text:
        return
    
    await bot.send_message(
        Config.DESTINATION_CHANNEL,
        text=update.text.html,
        parse_mode=enums.ParseMode.HTML
    )
    

