import datetime
from typing import Optional

def ntree_help():
    text = """
Ntree - Your Command Line Diary

Usage: diary [options] [arguments]

Basic Commands:
  -h, --help             Show this help message
  -n "text"              Create a new entry
  -l                     List all entries (latest 100)
  -t                     Show today's entries
  -d YYYY-MM-DD          Show entries for specific date

Advanced Features:
  --search "keyword"     Search entries containing keyword
  --fav                  Mark last entry as favorite
  --list-fav             List favorite entries
  --nostalgia [delay]    Show all entries chronologically with delay
                         (default delay: 2 seconds)

Examples:
  diary -n "Had a great day!"
  diary -d 2024-01-15
  diary --search "meeting"
  diary --nostalgia 1.5
"""
    print(text)

class Entry:
    def __init__(self, text: str, dt: Optional[datetime.datetime] = None, fav: bool = False):
        if not text or not text.strip():
            raise ValueError("Entry text cannot be empty")
            
        self.text = text.strip()
        self.dt = dt or datetime.datetime.now()
        self.time = self.dt.time()
        self.date = self.dt.date()
        self.fav = fav

    def __str__(self) -> str:
        return f"[{self.date}]({self.time.strftime('%H:%M:%S')}) {self.text}"

    def format_with_time(self) -> str:
        return f"[{self.time.strftime('%H:%M:%S')}] {self.text}"

    def format_with_date(self) -> str:
        return f"[{self.date}] {self.text}"

    def format_full(self) -> str:
        fav_mark = "★ " if self.fav else ""
        return f"[{self.date}]({self.time.strftime('%H:%M:%S')}) {fav_mark}{self.text}"