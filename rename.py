#!/usr/local/bin/python3
import os
import requests
import dotenv
import re

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

token= os.environ.get("SLACK_API_TOKEN")
def getChannelList():
    url_getlist = 'https://slack.com/api/channels.list'

    params = {
        "token": token 
    }

    res = requests.get(url_getlist, params=params)
    return res.json()['channels']

def renameChannel(channel_id, new_name):
    url_rename = "https://slack.com/api/channels.rename"

    params = {
        "token": token,
        "channel": channel_id,
        "name": new_name
    }
    res = requests.post(url_rename, params=params)

channels = getChannelList()

prefix_old = '70-toc'
prefix_new = '60-toc'

for channel in channels:
    if re.match(prefix_old, channel['name']):
        new_name = re.sub(prefix_old, prefix_new, channel['name'], count=1)
        print(channel['name'], '->', new_name)
        renameChannel(channel['id'], new_name)
