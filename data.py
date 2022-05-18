import sqlite3
import datetime

from diary import Entry

def set_entry(e):
	conn = sqlite3.connect("entries.db")
	c = conn.cursor()

	x = "INSERT INTO entry (content, id, d, t, fav) VALUES(?, ?, ?, ?, ?)"

	print(f"{e.date.isoformat()}{e.time.isoformat()}")

	y = (e.text, f"{e.date.isoformat()}{e.time.isoformat()}", e.date.isoformat(), e.time.isoformat(), 1 if e.fav else 0)

	c.execute(x,y)
	conn.commit()
	conn.close()

def get_entry(entry_id=None, limit=100, date=None, fav=False, first=False):
	conn = sqlite3.connect("entries.db")
	c = conn.cursor()

	if date != None:
		print(date.isoformat())
		c.execute(f"SELECT * FROM entry WHERE d={date.isoformat()}")
		fetched = c.fetchall()
	if entry_id != None:
		c.execute(f"SELECT * FROM entry WHERE id={entry_id}")
		fetched = c.fetchall()
	if fav:
		c.execute(f"SELECT * FROM entry WHERE fav={1 if fav else 0}")
		fetched = c.fetchall()
	else:
		c.execute(f'SELECT * FROM entry')
		fetched = c.fetchall()

	if first:
		fetched = fetched[:limit]
	else:
		fetched = fetched[-1 * limit:]

	conn.close()

	entry_list = []
	for i in fetched:
		date = datetime.date.fromisoformat(i[2])
		time = datetime.time.fromisoformat(i[3])
		dt = datetime.datetime.combine(date, time)
		fav = False if i[4] == 0 else True
		entry = Entry(i[0], dt, fav)
		entry_list.append(entry)

	return entry_list