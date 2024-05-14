import re
import os
import asyncio
import logging
from logging import WARNING, getLogger
from pyrogram import Client

LOGGER = getLogger(__name__)
LOGGER.setLevel(logging.INFO)
getLogger("pyrogram").setLevel(WARNING)

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    true_values = ["true", "yes", "1", "enable", "y"]
    false_values = ["false", "no", "0", "disable", "n"]
    if value.lower() in true_values:
        return True
    elif value.lower() in false_values:
        return False
    else:
        return default

def get_env(name, default=None):
    return os.environ.get(name, default)

# Bot information
SESSION = get_env('SESSION', 'Media_search')
API_ID = int(get_env('API_ID', ''))
API_HASH = get_env('API_HASH', '')
OWNER_ID = get_env('OWNER_ID', '6497757690')
BOT_TOKEN = get_env('BOT_TOKEN', "")

# Bot settings
CACHE_TIME = int(get_env('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled(get_env('USE_CAPTION_FILTER', 'true'))

PICS = get_env('PICS', 'https://graph.org/file/5e1f8888547a1a896a902.jpg https://graph.org/file/9649c1dcbae09f2e7700e.jpg').split()
NOR_IMG = get_env("NOR_IMG", "https://graph.org/file/549fd9f3272214acade82.jpg")
MELCOW_VID = get_env("MELCOW_VID", "https://graph.org/file/ccf3cbc4687263ac63420.jpg")
SPELL_IMG = get_env("SPELL_IMG", "https://graph.org/file/549fd9f3272214acade82.jpg")
SUBSCRIPTION = get_env('SUBSCRIPTION', 'https://graph.org/file/347c1f79f36d3cf14e0f5.jpg')
CODE = get_env('CODE', 'https://graph.org/file/02e7ecc3e2693b481b914.jpg')

# Command
COMMAND_HANDLER = get_env("COMMAND_HANDLER", "/")
PREFIX = get_env("PREFIX", "/")

# for eval function, work only in a specific group
EVAL_ID = get_env("EVAL_ID", "-1001566837125")

# Referal Settings
REFERAL_COUNT = int(get_env('REFERAL_COUNT', '20'))
REFERAL_PREMIUM_TIME = get_env('REFERAL_PREMIUM_TIME', '1 week')
OWNER_USERNAME = get_env('OWNER_USERNAME', 'sewxiy')

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in get_env('ADMINS', '6497757690 5115691197').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in get_env('CHANNELS', '-1001619818259').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in get_env('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in get_env('PREMIUM_USER', '6497757690').split()]
auth_channel = get_env('AUTH_CHANNEL', '') 
auth_grp = get_env('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = get_env('SUPPORT_CHAT_ID', '-1001566837125')
reqst_channel = get_env('REQST_CHANNEL_ID', '-1001905367057')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = is_enabled(get_env("NO_RESULTS_MSG", "false"))

# MongoDB information
DATABASE_URI = get_env('DATABASE_URI', "")
DATABASE_NAME = get_env('DATABASE_NAME', "")
COLLECTION_NAME = get_env('COLLECTION_NAME', 'Telegram_files')

DOWNLOAD_LOCATION = get_env("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

# chatgptAI
AI = is_enabled(get_env("AI", "True"), True)
OPENAI_API = get_env("OPENAI_API", "")
GOOGLE_API_KEY = get_env("GOOGLE_API_KEY", "")
AI_LOGS = int(get_env("AI_LOGS", "-1001868871195"))

# Auto approve
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in get_env('CHAT_ID', '').split()]
TEXT = get_env("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @codflix_bots</b>")
APPROVED = is_enabled(get_env("APPROVED_WELCOME", "true"), True)

# stream link shortener
STREAM_SITE = get_env('STREAM_SITE', 'shareus.io')
STREAM_API = get_env('STREAM_API', '')
STREAMHTO = get_env('STREAMHTO', 'https://t.me/How_to_Download_7x/32')

# Verify
VERIFY = is_enabled(get_env('VERIFY', "false"), False)
HOWTOVERIFY = get_env('HOWTOVERIFY', 'https://t.me/How_to_Download_7x/26')

# Others
SHORTLINK_URL = get_env('SHORTLINK_URL', '')
SHORTLINK_API = get_env('SHORTLINK_API', '')
IS_SHORTLINK = is_enabled(get_env('IS_SHORTLINK', "false"), False)
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in get_env('DELETE_CHANNELS', '').split()]
MAX_B_TN = get_env("MAX_B_TN", "5")
MAX_BTN = is_enabled(get_env('MAX_BTN', "true"), True)

APP_NAME = ''
if 'DYNO' in os.environ:
    ON_HEROKU = True
    APP_NAME = get_env('APP_NAME')

else:
    ON_HEROKU = False
HAS_SSL = bool(getenv('HAS_SSL', True))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN, PORT)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing IMDb details for your queries.\n" if IMDB else "IMDB Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found, Users will be redirected to send /start to Bot PM instead of sending a file directly.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled, files will be sent in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and file size will be shown in a single button instead of two separate buttons.\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled, filename and file_size will be shown as different buttons.\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be sent along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of the file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled.\n" if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled, the plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, the bot will be suggesting related movies if a movie is not found.\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled.\n")
LOG_STR += (f"MAX_LIST_ELM Found, the long list will be shortened to the first {MAX_LIST_ELM} elements.\n" if MAX_LIST_ELM else "The full list of casts and crew will be shown in the IMDb template, restrict them by adding a value to MAX_LIST_ELM.\n")
LOG_STR += f"Your current IMDb template is {IMDB_TEMPLATE}."

# Now, you can use these variables wherever you need them in your code.
