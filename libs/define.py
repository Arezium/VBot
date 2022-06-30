import random
import os
from itertools import cycle

user_agents = cycle(open("libs/utils/user_agents.txt", "r").read().splitlines())
proxies = open("libs/utils/proxies.txt", "r").read().splitlines()
API_URL = "https://discord.com/api/v9"


def getAliases(command):
  aliases = {
    "spamall": [
        "sall"
    ],

    "blockspam": [
        "bs",
        "bspam"
    ],
    
    "channelcreate": [
        "cc",
        "chancr",
        "ccr",
        "ccreate",
        "chcr"
    ],
    
    "channeldelete": [
        "cd",
        "chandel",
        "cdel",
        "cdelete",
        "chdel"
    ],

    "rolecreate": [
        "rc",
        "rolecr",
        "rcreate"
    ],

    "roledelete": [
        "rd",
        "roledel",
        "rdel",
        "rdelete"
    ],

    "nuke": [
        "destroy",
        "hack"
    ],

    "logout": [
        "exit",
        "quit",
        "out",
        "off"
    ],

    "eval": [
        "evaluate",
        "exec",
        "execute",
        "run",
        "code"
    ],

    "ping": [
        "lat",
        "latency",
        "speed"
    ],

    "clear": [
        "purge",
        "clean",
        "erase"
    ],

    "stealpfp": [
        "getpfp"
    ],
    
    "tokengrab": [
        "tgrab",
        "gettoken",
        "otax",
        "token-grab",
        "token"
    ],
    
    "ip": [
        "ipgrab",
        "dox",
        "getip",
        "grabip"
    ],

    "user": [
        "u"
    ],

    "server": [
        "s"
    ],
    
    "gen": [
        "generate",
        "make",
        "fake"
    ],
    
    "backup-f": [
        "backup-friends",
        "friends-backup",
        "backupf"
    ],

    "stopactivity": [
        "stopstatus",
        "stopact",
        "stopst"
    ]
  }
  
  return aliases[command]

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
      
    return text

def headers(bot_token):
    return {
        "authorization": bot_token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-US,en;q=0.9,it-IT;q=0.8,it;q=0.7,en-GB;q=0.6",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": next(user_agents)
    }

def clearConsole():
  os.system("clear" if os.name != "nt" else "cls")
