from motor.motor_asyncio import AsyncIOMotorClient

from PyroUbot.config import MONGO_URL

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongodb = mongo_client.userbotxx

from .two_factor import set_two_factor, get_two_factor
from PyroUbot.core.database.expired import *
from PyroUbot.core.database.userbot import *
from PyroUbot.core.database.pref import *
from PyroUbot.core.database.variabel import *
from PyroUbot.core.database.antigcast import *
