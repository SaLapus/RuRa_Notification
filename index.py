import requests
import json

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

        
