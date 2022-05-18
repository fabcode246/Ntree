import sqlite3



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
