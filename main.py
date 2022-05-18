import sys, os
from diary import Entry, ntree_help
from data import get_entry, set_entry
import datetime
from time import sleep

if len(sys.argv) < 2:
    ntree_help()
    sys.exit()
elif sys.argv[1] in ("-h", "--help"):
    ntree_help()
    sys.exit()
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
elif sys.argv[1] == '-d':
    text = ""
    entries = get_entry(date=datetime.date.fromisoformat(sys.argv[2]))
    for e in entries:
        text += f"[{e.time.strftime('%X')}] {e.text}\n"
    print(text)
    sys.exit()
elif sys.argv[1] == '--nostalgia':
    if len(sys.argv) > 2:
        delay = float(sys.argv[2])
    else:
        delay = 2
    entries = get_entry(limit=100000000000, first=True)
    os.system('cls' if os.name=='nt' else 'clear')
    for i in entries:
        print(f'[{i.date}]({i.time}) {i.text}')
        sleep(delay)
        os.system('cls' if os.name=='nt' else 'clear')
elif sys.argv[1] == '-l':
	entries = get_entry()
	print(entries)