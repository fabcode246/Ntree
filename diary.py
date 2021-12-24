# Ntree

import sqlite3
import sys
import datetime
import random as r

'''
conn = sqlite3.connect("entries.db")
c = conn.cursor()


c.execute("DROP TABLE IF EXISTS entry")


c.execute("""CREATE TABLE entry ( 
           content text,
           id text,
           d text,
           t text,
           fav integer
       )""")

print(c)

conn.commit()
conn.close()
'''

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
        conn = sqlite3.connect("entries.db")
        c = conn.cursor()

        c.execute(f"SELECT id FROM entry WHERE id={text}")
        fetched = c.fetchone()
        conn.close()
        if not fetched:
            return text

def set_entry(e):
    conn = sqlite3.connect("entries.db")
    c = conn.cursor()

    x = "INSERT INTO entry (content, id, d, t, fav) VALUES(?, ?, ?, ?, ?)"

    y = (e.text, e.id, e.date.isoformat(), e.time.isoformat(), 1 if e.fav else 0)

    c.execute(x,y)
    conn.commit()
    conn.close()
    

def get_entry(entry_id=None, limit=100, date=None, fav=False, first=False):
    conn = sqlite3.connect("entries.db")
    c = conn.cursor()

    if date != None:
        c.execute(f"SELECT * FROM entry WHERE d={date.isoformat()}")
        fetched = c.fetchall()
    if entry_id != None:
        c.execute(f"SELECT * FROM entry WHERE id={entry_id}")
        fetched = c.fetchall()
    if fav:
        c.execute(f"SELECT * FROM entry WHERE fav={1 if fav else 0}")
        fetched = c.fetchall()
    
    if first:
        fetched = fetched[:limit]
    else:
        fetched = fetched[-1 * limit:]

    conn.close()

    entry_list = []
    for i in fetched:
        print(i)

# def text_maker:

# combine date and time into datetime before
class Entry:
    def __init__(self, text, dt=datetime.datetime.now(), fav=False, entry_id=None):
        self.id = id_gen() if entry_id == None else entry_id
        self.text = str(text)
        self.dt = dt
        self.time = dt.time()
        self.date = dt.date()
        self.fav = fav

if len(sys.argv) < 2:
    help()
elif sys.argv[1] in ("-h", "--help"):
    help()
elif sys.argv[1] == "-n":
    set_entry(Entry(text=sys.argv[2]))
    print("new entry created!!!")
    sys.exit()
elif sys.argv[1] == "-t":
    text = ""
    entries = get_entry(date=datetime.date.today())
    for e in entries:
        text += f"[{e.time}] {e.text}"
    print(text)
    sys.exit()

