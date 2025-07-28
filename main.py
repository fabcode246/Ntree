import sys
import os
from typing import List
from diary import Entry, ntree_help
from data import db
import datetime
from time import sleep

def display_entries(entries: List[Entry], show_date: bool = True) -> None:
    if not entries:
        print("No entries found.")
        return

    current_date = None
    for entry in entries:
        if show_date and entry.date != current_date:
            current_date = entry.date
            print(f"\n=== {current_date} ===\n")
        print("  " + (entry.format_full() if show_date else entry.format_with_time()))

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        ntree_help()
        return

    command = sys.argv[1]

    try:
        if command == "-n":
            if len(sys.argv) < 3:
                print("Error: No text provided for new entry")
                return
            entry = Entry(text=" ".join(sys.argv[2:]))
            if db.add_entry(entry):
                print("New entry created successfully!")
            else:
                print("Failed to create entry")

        elif command == "-t":
            entries = db.get_entries(date=datetime.date.today())
            display_entries(entries, show_date=False)

        elif command == "-d":
            if len(sys.argv) < 3:
                print("Error: No date provided. Format: YYYY-MM-DD")
                return
            try:
                target_date = datetime.date.fromisoformat(sys.argv[2])
                entries = db.get_entries(date=target_date)
                display_entries(entries, show_date=False)
            except ValueError:
                print("Error: Invalid date format. Use YYYY-MM-DD")

        elif command == "--nostalgia":
            delay = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
            entries = db.get_entries(limit=100000000000, first=True)
            os.system('cls' if os.name=='nt' else 'clear')
            for entry in entries:
                print(entry.format_full())
                sleep(delay)
                os.system('cls' if os.name=='nt' else 'clear')

        elif command == "-l":
            entries = db.get_entries()
            display_entries(entries)

        elif command == "--search":
            if len(sys.argv) < 3:
                print("Error: No search keyword provided")
                return
            keyword = sys.argv[2]
            entries = db.search_entries(keyword)
            display_entries(entries)

        elif command == "--fav":
            # Mark the last entry as favorite
            entries = db.get_entries(limit=1)
            if not entries:
                print("No entries to mark as favorite")
                return
            entry = entries[0]
            entry.fav = True
            if db.add_entry(entry):
                print("Entry marked as favorite!")
            else:
                print("Failed to mark entry as favorite")

        elif command == "--list-fav":
            entries = db.get_entries(fav=True)
            display_entries(entries)

        else:
            print(f"Unknown command: {command}")
            ntree_help()

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()