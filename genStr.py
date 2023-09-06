#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG


import os

print("an online StringSession generator")

print("[p]: Pyrogram (docs.pyrogram.org)")
print("PyroGramBot ==> https://GitHub.com/SpEcHiDe/PyroGramBot")

print("[pv2]: Pyrogram (docs.pyrogram.org)")
print("PyroGramBot ==> https://docs.pyrogram.org/releases/v2.0")

print("[t]: Telethon (docs.telethon.dev)")
print("Telethon UserBot ==> https://GitHub.com/SpEcHiDe/UniBorg")

print("Select your required option: ")
s_l = input("enter p / pv2 / t ==> ")

print(
    "should the string be sent in a Tg Saved Messages OR printed to STDOUT here:? "
)
weirdCheck = input("enter tg / p ==> ") == "tg"

if s_l == "p":
	os.system("pip uninstall -y pyrogram && pip install pyrogram==1.3.5")
	print("you selected Pyrogram")
	APP_ID = int(input("Enter APP ID here: "))
	API_HASH = input("Enter API HASH here: ")
	import pyrogram
	app = pyrogram.Client(":memory:",
	                      api_id=APP_ID,
	                      api_hash=API_HASH,
	                      parse_mode="html")
	app.start()
	session_str = app.export_session_string()
	if weirdCheck:
		s_m = app.send_message("me", session_str)
		s_m.reply_text(
		    ("⬆️ This <code>1.3.5</code> StringSession is generated using "
		     "https://replit.com/@SpEcHiDe/GenerateStringSession\n"
		     "Please subscribe @UniBorg "),
		    quote=True)
	else:
		print(session_str)
	app.stop()

	print("please check your Telegram Saved Messages for the StringSession ")

elif s_l == "t":
	os.system(
	    "pip uninstall -y telethon && pip install https://github.com/TelegramPlayGround/Telethon/archive/ad5d30a.zip"
	)
	print("you selected Telethon")
	# (c) https://t.me/TelethonChat/37677
	from telethon.sync import TelegramClient
	from telethon.sessions import StringSession
	APP_ID = int(input("Enter APP ID here: "))
	API_HASH = input("Enter API HASH here: ")
	client = TelegramClient(StringSession(), APP_ID, API_HASH)
	client.start()
	session_str = client.session.save()
	if weirdCheck:
		s_m = client.send_message("me", session_str)
		s_m.reply(("⬆️ This StringSession is generated using "
		           "https://replit.com/@SpEcHiDe/GenerateStringSession\n"
		           "Please subscribe @UniBorg "))
	else:
		print(session_str)
	client.disconnect()
	print("please check your Telegram Saved Messages for the StringSession ")

elif s_l == "pv2":
	os.system("pip uninstall -y pyrogram && pip install pyrogram==2.0.106")
	print("you selected Pyrogram")
	APP_ID = int(input("Enter APP ID here: "))
	API_HASH = input("Enter API HASH here: ")
	import pyrogram
	app = pyrogram.Client("user",
	                      api_id=APP_ID,
	                      api_hash=API_HASH,
	                      in_memory=True,
	                      parse_mode=pyrogram.enums.ParseMode.HTML)
	app.start()
	session_str = app.export_session_string()
	if weirdCheck:
		s_m = app.send_message("me", session_str)
		s_m.reply_text(
		    ("⬆️ This <code>2.0.30</code> StringSession is generated using "
		     "https://replit.com/@SpEcHiDe/GenerateStringSession\n"
		     "Please subscribe @UniBorg "),
		    quote=True)
	else:
		print(session_str)
	app.stop()
	print("please check your Telegram Saved Messages for the StringSession ")

else:
	print("please select only p / pv2 / t, thank you.")
