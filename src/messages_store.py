import json
from dataclasses import dataclass
from datetime import datetime

#PATH = r"..\..\gbook\store"
PATH = r"D:\CODING\OpenServer\domains\web_spec\gbook\store"
DB = PATH + "\messages.json"

def add_message(name, email, message):
    time_at = datetime.now().replace(microsecond = 0)
    messages[time_at] = {"name": name, "email": email, "msg": message}
    flush()
    return time_at

def delete_message(time):
    if isinstance(time, (str, int)):
        time = datetime.fromtimestamp(int(time))
    del messages[time]
    flush()

def flush():
    to_flush = dict(messages)
    for date in list(to_flush.keys()):
        message = to_flush[date]
        del to_flush[date]
        to_flush[int(date.timestamp())] = message
    with open(DB, 'w', encoding='utf-8') as f:
        json.dump(to_flush, f)

def by_date():
    """ return [[id, msg, email, name], ...] """
    keys = sorted(messages.keys(), reverse=True)
    return [(
        id,
        messages[id]['name'],
        messages[id]['email'],
        messages[id]['msg'],
    ) for id in keys]


try:
    with open(DB, 'r', encoding='utf-8') as f:
        pass
except FileNotFoundError:
    with open(DB, 'w', encoding='utf-8') as f:
        json.dump({}, f)

with open(DB, 'r', encoding='utf-8') as f:
    messages = json.load(f)
    for key in list(messages.keys()):
        message = messages[key]
        del messages[key]
        messages[datetime.fromtimestamp(int(key))] = message

