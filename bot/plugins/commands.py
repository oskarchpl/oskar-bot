#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import asyncio
import time
import sys
import psutil

from pyrogram import Client, filters, enums
from pyrogram.types import Message

from bot import LOGGER, Config


logger = LOGGER(__name__)


@Client.on_message(filters.command(["start"]) & filters.user(Config.AUTH_USERS))
async def start (bot, update):
    
    await update.edit("Bot Started..! And its Up and Running..!")


@Client.on_message(filters.private & filters.command(["help"]) & filters.user(Config.AUTH_USERS))
async def help(bot, update):
    
    await update.edit(
        "Avaliable Commands:\n\n"\
        "/start - Check if bot alive\n"\
        "/clone - Clone messages from target channel to destination channel\n"\
        "/help - Show this menu\n"\
        "/stats - Show bot statistics\n"\
        "/restart - Restart the bot\n"\
        "/logs - Get bot logs\n\n"\

    )


@Client.on_message(filters.private & filters.command(["stats"]) & filters.user(Config.AUTH_USERS))
async def stats(bot, update: Message):


    msg = await update.edit(
        text="__Processing...__",
        parse_mode=enums.ParseMode.MARKDOWN
    )

    currentTime = time.strftime("%Hh%Mm%Ss", time.gmtime(
        time.time() - Config.BOT_START_TIME))
    cpu_usage = psutil.cpu_percent()

    memory = psutil.virtual_memory()
    storage = psutil.disk_usage('/')

    memory_stats = f"RAM Usage: {convert_size(memory.used)} / {convert_size(memory.total)} ({memory.percent}%)"
    storage_stats = f"Storage Usage: {convert_size(storage.used)} / {convert_size(storage.total)} ({storage.percent}%)"

    ms_g = f"<b><u>Bot Stats</b></u>\n" \
        f"<code>Uptime: {currentTime}</code>\n"\
        f"<code>CPU Usage: {cpu_usage}%</code>\n"\
        f"<code>{memory_stats}</code>\n"\
        f"<code>{storage_stats}</code>\n\n"

    await msg.edit_text(
        text=ms_g,
        parse_mode=enums.ParseMode.HTML
    )


@Client.on_message(filters.private & filters.command(["restart"]) & filters.user(Config.AUTH_USERS))
async def restart(bot, update):

    b = await update.edit(
        text="__Restarting.....__",
        parse_mode=enums.ParseMode.MARKDOWN
    )
    await asyncio.sleep(3)
    await b.delete()
    os.system("git pull")
    os.remove("logs.txt")
    os.execl(sys.executable, sys.executable, "-m", "bot")


@Client.on_message(filters.command(['logs']) & filters.user(Config.AUTH_USERS))
async def send_logs(_, m):
    await m.reply_document(
        "logs.txt",
        caption='Logs'
    )
    await m.delete()



def convert_size(size):
    units = ["B", "KB", "MB", "GB", "TB"]
    index = 0
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1
    return f"{size:.2f} {units[index]}"

