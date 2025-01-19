from telethon.sync import TelegramClient
from telethon import *
import time
import requests
import re
import json
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import PeerChannel
from telethon import TelegramClient, Button, events
import logging
from prettytable import PrettyTable

api_id = 21381591  # Your API ID
api_hash = '1fd701477d5e7e38adc1fc6fa68b7dd5'  # Your API Hash

def lista(dets):
    dets = str(dets)
    arrays = re.findall(r'[0-9]+', dets)
    return arrays

client = TelegramClient("ssshl", api_id, api_hash)
client2 = TelegramClient("bothg", api_id, api_hash)
client.start()
client2.start()

def RoldexVerseCcs(id):
    id = str(id)
    with open('UltraVerseCcs.txt', 'w') as f:
        if f.write(id):
            return True
        else:
            return False

global str

with client:
    print("started")
    while True:
        try:
            req = requests.Session()
            f = open('UltraVerseCcs.txt', 'r')
            rd = int(f.read())
            channelList = [
                "https://t.me/Ripplz",
                "https://t.me/rambhaktscrap",
                "https://t.me/AtriScrapper",
                "https://t.me/AyaneDropS",
                "https://t.me/HumanOFC",
                "https://t.me/scrapccdump",
                "https://t.me/RavenApproved_ccs",
                "https://t.me/nastyscr",
                "https://t.me/BinnersHub"
            ]
            fornum = len(channelList)
            for i in range(0, fornum):
                # Iterate over messages in the channel
                async for message in client.iter_messages(channelList[i], min_id=rd, wait_time=5):
                    msg = message.text
                    if len(msg) == 0:
                        raise Exception('empty data')
                    else:
                        input = re.findall(r"[0-9]+", message.text)
                        try:
                            if len(input) == 0 or len(input) == 2:
                                raise Exception("Invalid Data")
                            elif len(input) > 4 and len(input[1]) < 2:
                                cc = input[0]
                                mes = input[1]
                                ano = input[2]
                                cvv = input[3]
                            elif len(input[1]) == 3:
                                ano1 = input[2]
                                cc = input[0]
                                mes = input[2]
                                cvv = input[1]
                                ano = input[3]
                                if len(mes) > 3:
                                    mes1 = mes
                                    cc = cc
                                    cvv = cvv
                                    mes = mes[:2]
                                    ano = mes1[2:]
                            elif len(input[1]) > 3:
                                ano1 = input[2]
                                cc = input[0]
                                cvv = input[2]
                                mes = input[1][:2]
                                ano = input[1][2:]
                            elif len(input[0]) < 15:
                                raise Exception('Invalid data')
                            else:
                                cc = input[0]
                                mes = input[1]
                                ano = input[2]
                                cvv = input[3]
                        except Exception as e:
                            print(e)
                        else:
                            lista = f"<code>{cc}|{mes}|{ano}|{cvv}</code>"
                            apibinlist = json.loads(requests.get(f"https://lookup.binlist.net/{cc}").text)
                            binEmoji = apibinlist["country"]["emoji"]
                            binName = apibinlist["country"]["name"]
                            binType = apibinlist["type"]
                            binBank = apibinlist["bank"]["name"]
                            respo = f"""
{lista} - {binBank} - {binEmoji} 
@SatsNova"""

                            # Send the response to your channel
                            client2.send_message(-1002435914891, respo, parse_mode='html')

                    # Update the record of the last message ID
                    wd = RoldexVerseCcs(message.id)

        except errors.FloodWaitError as e:
            print('Have to sleep', e.seconds, 'seconds')
            time.sleep(e.seconds)
        except Exception as e:
            print(e)
