import requests
import json

import db

f = open('data.json',)
data = json.load(f)
f.close()


def getLPObserver():

    r = requests.get(
        'https://api.vk.com/method/groups.getLongPollServer', params=data)
    res = r.json()['response']

    LPPayload = {
        'act': 'a_check',
        'key': f'{res["key"]}',
        'ts': f'{res["ts"]}',
        'wait': '25'
    }

    LPServer = res['server']

    print("Server is created")



    def getUpdates():
        req = requests.get(f'{LPServer}', params=LPPayload)

        print("getUpdate")

        res = req.json()

        print(list(res))

        LPPayload['ts'] = res['ts']

        print("failed:")
        print("failed" in res)

        if("failed" in res and res['failed'] == 1):
            return getUpdates()

        return res['updates']

    return getUpdates


def sendNotifications(title):

    users = 'next string'
    db.getTitleSubscribers(title)

    for user in users:
        sendMessage(user, "New cahptre")


def sendMessage(user_id, message):

    random_id = db.getRandomID(user_id)

    payload = {
        'user_id': f'{user_id}',
        'random_id': f'{random_id}',
        'peer_id': f'{user_id}',
        'message': f'{message}'
    }

    for value, index in data.items():
        payload[index] = value

    r = requests.get('https://api.vk.com/method/messages.send', params=payload)

    print(r.json())
