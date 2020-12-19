import json
import re

import requests

import bot


def logItem(item):
    f = open("log.txt", "a")
    f.write(json.dumps(item, indent=5))
    f.write('\n')
    f.close()


Updater = bot.getLPObserver()

x = 0
while True:
    x = x + 1
    print(f'#{x}')

    updates = Updater()

    for item in updates:
        logItem(item)

        if item["type"] == "wall_post_new":
            post = item['object']

            p = re.compile('https://ruranobe.ru/r/(.*?)/')
            link = p.search(post['text'])

            if link is not None:
                title = link.group(1)
                print(title)
                bot.sendNotifications(
                    title, wall_post={'media_id': post['id'], 'owner_id': post['owner_id']})
        elif item["type"] == "message_new":
            message = item['object']['message']

            # bot.sendMessage(
            #     user_id=message['from_id'], random_id=message, message=message['text'])
