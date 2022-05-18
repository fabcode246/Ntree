import sys
from diary import Entry, ntree_help
from data import get_entry, set_entry
import datetime
#import sqlite3


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
        text += f"[{e.time.strftime('%X')}] {e.text}\n"
    print(text)
    sys.exit()
elif sys.argv[1] == '-l':
	entries = get_entry()
	print(entries)