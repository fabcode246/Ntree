# Ntree

#import sys
import datetime



def ntree_help():
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



# def text_maker:

# combine date and time into datetime before
class Entry:
    def __init__(self, text, dt=datetime.datetime.now(), fav=False):
        self.text = str(text)
        self.dt = dt
        self.time = dt.time()
        self.date = dt.date()
        self.fav = fav

'''if len(sys.argv) < 2:
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

'''