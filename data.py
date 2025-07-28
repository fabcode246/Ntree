import sqlite3
import datetime
from typing import List, Optional
from diary import Entry

class DiaryDatabase:
    def __init__(self, db_path: str = "entries.db"):
        self.db_path = db_path

    def _get_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def add_entry(self, entry: Entry) -> bool:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO entry (content, id, d, t, fav) VALUES (?, ?, ?, ?, ?)",
                    (entry.text,
                     f"{entry.date.isoformat()}{entry.time.isoformat()}",
                     entry.date.isoformat(),
                     entry.time.isoformat(),
                     1 if entry.fav else 0)
                )
                return True
        except sqlite3.Error as e:
            print(f"Error adding entry: {e}")
            return False

    def get_entries(self,
                    entry_id: Optional[str] = None,
                    date: Optional[datetime.date] = None,
                    fav: bool = False,
                    limit: int = 100,
                    first: bool = False) -> List[Entry]:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                query = "SELECT * FROM entry"
                params = []

                if date:
                    query += " WHERE d = ?"
                    params.append(date.isoformat())
                elif entry_id:
                    query += " WHERE id = ?"
                    params.append(entry_id)
                elif fav:
                    query += " WHERE fav = 1"

                cursor.execute(query, params)
                rows = cursor.fetchall()

                if first:
                    rows = rows[:limit]
                else:
                    rows = rows[-limit:]

                return [
                    Entry(
                        text=row[0],
                        dt=datetime.datetime.combine(
                            datetime.date.fromisoformat(row[2]),
                            datetime.time.fromisoformat(row[3])
                        ),
                        fav=bool(row[4])
                    ) for row in rows
                ]
        except sqlite3.Error as e:
            print(f"Error retrieving entries: {e}")
            return []

    def search_entries(self, keyword: str, limit: int = 100) -> List[Entry]:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM entry WHERE content LIKE ? ORDER BY d DESC, t DESC LIMIT ?",
                    (f"%{keyword}%", limit)
                )
                rows = cursor.fetchall()
                return [
                    Entry(
                        text=row[0],
                        dt=datetime.datetime.combine(
                            datetime.date.fromisoformat(row[2]),
                            datetime.time.fromisoformat(row[3])
                        ),
                        fav=bool(row[4])
                    ) for row in rows
                ]
        except sqlite3.Error as e:
            print(f"Error searching entries: {e}")
            return []

# Create a global instance for easy access
db = DiaryDatabase()