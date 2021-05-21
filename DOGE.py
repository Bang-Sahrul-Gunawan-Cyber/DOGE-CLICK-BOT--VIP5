from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import (
    GetHistoryRequest,
    GetBotCallbackAnswerRequest,
)
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep
import json, re, sys, os

try:
    import requests
    import webbrowser
    from bs4 import BeautifulSoup
except:
    print(
        "\033[1;30m# \033[1;31mHmmm Looks like the Requests And Bs4 Module Is Not Installed\n\033[1;30m# \033[1;31mTo install Please Type pip install requests and pip install bs4"
    )
    sys.exit()

c = requests.Session()

banner = """
\033[0;31m██████╗  ██████╗  ██████╗ ███████╗    ██████╗  ██████╗ ████████╗
\033[0;31m██╔══██╗██╔═══██╗██╔════╝ ██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝
\033[0;31m██║  ██║██║   ██║██║  ███╗█████╗      ██████╔╝██║   ██║   ██║
\033[0;37m██║  ██║██║   ██║██║   ██║██╔══╝      ██╔══██╗██║   ██║   ██║
\033[0;37m██████╔╝╚██████╔╝╚██████╔╝███████╗    ██████╔╝╚██████╔╝   ██║
\033[0;37m╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝    ╚═════╝  ╚═════╝    ╚═╝
\033[0;31m<▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬>
"""
if not os.path.exists("session"):
    os.makedirs("session")
 
if len(sys.argv) < 2:
    print("\033[1;33mCommand Input: python DOGE.py +62")
    sys.exit(1)

def tunggu(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(x, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(
            "\033[1;30m#\033[1;0m{:2d} \033[1;32mseconds remaining".format(remaining)
        )
        sys.stdout.flush()
        sleep(1)

# UA USER AGENT
ua = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 7.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"
}

# API ID
api_id = 717425
# API HASH
api_hash = "322526d2c3350b1d3530de327cf08c07"
phone_number = sys.argv[1]

client = TelegramClient("session/" + phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone_number)       
        me = client.sign_in(phone_number, input(' Type OTP : '))
    except SessionPasswordNeededError:
        passw = input('Your 2fa Password : ')
        me = client.start(phone_number, passw)
myself = client.get_me()
os.system("clear") 
print(banner)
print(
    "\033[1;32mWelcome to the DOGE Pro Bot",
    myself.first_name,
    "\n\033[1;32mThis Tool Is Used To Automate DOGE Click Bot",
)

print("\n\n\033[1;37mBot Is Running......!")
try:
        channel_entity = client.get_entity("@Dogecoin_click_bot")
        channel_username = "@Dogecoin_click_bot"
        for i in range(5000000):
            sys.stdout.write("\r")
            sys.stdout.write(
                "                                                              "
            )
            sys.stdout.write("\r")
            sys.stdout.write("\033[1;30m# \033[1;33mTrying to Visit Url")
            sys.stdout.flush()
            client.send_message(entity=channel_entity, message="🖥 Visit sites")
            sleep(3)
            posts = client(
                GetHistoryRequest(
                    peer=channel_entity,
                    limit=1,
                    offset_date=None,
                    offset_id=0,
                    max_id=0,
                    min_id=0,
                    add_offset=0,
                    hash=0,
                )
            )
            if (
                posts.messages[0].message.find("Sorry, there are no new ads available")
                != -1
            ):
                print('\n\033[1;31mAds are Out. Try Again Later. Program Exiting........\n')
                client.send_message(entity=channel_entity, message="💰 Balance")
                sleep(5)
                posts = client(
                    GetHistoryRequest(
                        peer=channel_entity,
                        limit=1,
                        offset_date=None,
                        offset_id=0,
                        max_id=0,
                        min_id=0,
                        add_offset=0,
                        hash=0,
                    )
                )
                message = posts.messages[0].message
                print('\033[0;32m' + message)
                print('\033[0;0m' + ' ')
                sys.exit()
            else:
                try:
                    url = posts.messages[0].reply_markup.rows[0].buttons[0].url
                    sys.stdout.write("\r")
                    sys.stdout.write("\033[1;32m• \033[1;33mVisit " + url)
                    sys.stdout.flush()
                    id = posts.messages[0].id
                    webbrowser.open(url) 
                    
                    sleep(5)
                    posts = client(
                            GetHistoryRequest(
                                peer=channel_entity,
                                limit=1,
                                offset_date=None,
                                offset_id=0,
                                max_id=0,
                                min_id=0,
                                add_offset=0,
                                hash=0,
                            )
                        )
                
                    message = posts.messages[0].message

                    if (
                            posts.messages[0].message.find("You must stay") != -1
                            or posts.messages[0].message.find("Please stay on") != -1 
                    ):
                            sec = re.findall(r"([\d.]*\d+)", message)
                            tunggu(int(sec[0]))
                            sleep(1)
                            posts = client(
                                GetHistoryRequest(
                                    peer=channel_entity,
                                    limit=2,
                                    offset_date=None,
                                    offset_id=0,
                                    max_id=0,
                                    min_id=0,
                                    add_offset=0,
                                    hash=0,
                                )
                            )
                            messageres = posts.messages[1].message
                            sleep(2)
                            sys.stdout.write("\r\033[1;30m# \033[1;32m" + messageres + "\n")

                    else:
                             Deftime = '120'
                             sys.stdout.write("\n" + "External Site Timer Detected. Waiting Default " + Deftime + " Sec." + "\n")
                             sec = re.findall(r"([\d.]*\d+)", Deftime)
                             tunggu(int(sec[0]))
                             sleep(1)
                             posts = client(
                                 GetHistoryRequest(
                                     peer=channel_entity,
                                     limit=2,
                                     offset_date=None,
                                     offset_id=0,
                                     max_id=0,
                                     min_id=0,
                                     add_offset=0,
                                     hash=0,
                                 )
                             )
                             messageres = posts.messages[1].message
                             sleep(2)
                             sys.stdout.write("\r\033[1;30m# \033[1;32m" + messageres + "\n")

                except Exception as e:
                             sys.stdout.write("Unexpected Error. " + str(e) + "\n")

finally: 
   client.disconnect()
