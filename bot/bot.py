#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import logging
import asyncio

from typing import Union, Optional, AsyncGenerator

from pyrogram import Client, enums, __version__, types
from pyrogram.errors import FloodWait
from pyropatch import listen, flood_handler

from bot import LOGGER, Config


class Bot(Client):

    def __init__(self):
        super().__init__(
            "bot",
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            plugins={
                "root": "bot/plugins"
            },
            workers=400,
            session_string=Config.USER_SESSION,
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        self.me = await self.get_me()
        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"@{self.me.username}  started! "
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")

    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            try:
                messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            except FloodWait as e:
                logging.info(f"Sleeping for {e.value} seconds")
                await asyncio.sleep(e.value)
                messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))

            for message in messages:
                yield message
                current += 1

