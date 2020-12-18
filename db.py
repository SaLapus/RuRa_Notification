import sqlite3

connection = sqlite3.connect("users.sqlite")

cursor = connection.cursor()


def getRandomID(user_id):
    random_id = 0

    cursor.execute(f'SELECT random_id FROM t WHERE user_id={user_id}')
    results = cursor.fetchall()

    print(f'SELECT random_id FROM t WHERE user_id={user_id}')
    print(results)

    random_id = results[0][0]

    if len(results) == 0:
        cursor.execute(f'INSERT INTO t VALUES({user_id}, 0)')
        results = cursor.fetchall()

        print(f'INSERT INTO t VALUES({user_id}, 0)')
        print(results)

        random_id = 0

        connection.commit()

    cursor.execute(
        f'INSERT OR REPLACE INTO t VALUES({user_id}, {random_id + 1})')
    results = cursor.fetchall()
    connection.commit()

    return random_id


def getTitleSubscribers(title):
    cursor.execute(f'SELECT user_ids FROM subs WHERE title="{title}"')
    results = cursor.fetchall()

    return results[0][0].split(',')


def addTitleSubscriber(title, user_id):
    cursor.execute(f'SELECT user_ids FROM subs WHERE title="{title}"')
    results = cursor.fetchall()

    users = results[0][0] + f',{user_id}'

    cursor.execute(f'INSERT OR REPLACE INTO subs VALUES("{title}", "{users}")')
    results = cursor.fetchall()
    connection.commit()

    return True
