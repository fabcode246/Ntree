# DIARY

import pymongo
import sys
import datetime
import random as r

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["dairy"]

entry = db['entry']

def help():
    text = """DIARY
    usage: diary -h [options]
    -h help message
    -n "text here" create a new entry
    -l list entries(max=100)
    -t list today's entries only
    -d [date] list entries of a specific date
    --nostalgia [delay(default=0.5s)] shows all your entries one by one in chronological order"""
    print(text)
    sys.exit()

def id_gen():
    while True:
        text = ""
        for i in range(24):
            text += str(r.randint(0,9))
        finds = entry.find({"id": text})
        if len(finds) == 0:
            return int(text)

def set_entry(e):
    global entry
    new_entry = {
    "id": e.id,
    "text": e.text,
    "date": e.date,
    "time": e.time,
    "fav": e.fav
    }
    entry.insert_one(new_entry)

class Entry:
    def __init__(self, text, date=datetime.date.today(), time=None, fav=False, id=None):
        self.id = id_gen()
        self.text = text
        self.date = date
        now = datetime.datetime.now()
        self.time = datetime.time(int(now.strftime("%H")), int(now.strftime("%M")), int(now.strftime("%S")))
        self.fav = fav

if len(sys.argv) < 2:
    help()
elif sys.argv[1] in ("-h", "--help"):
    help()
elif sys.argv[1] == "-n":
    set_entry(Entry(sys.argv[2]))