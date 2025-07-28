# Ntree - Your Command Line Diary

Ntree is a lightweight, command-line diary application that allows you to quickly create and manage diary entries without opening any external applications. It's designed for efficiency and ease of use, perfect for keeping track of your daily thoughts and activities.

## Features

- Quick entry creation from command line
- View entries by date or today's entries
- Search through entries
- Mark entries as favorites
- Nostalgia mode to review past entries
- Organized entry display with dates and timestamps
- SQLite database for reliable storage

## Installation

### Prerequisites

- Python 3.6 or higher
- SQLite3 (usually comes with Python)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ntree.git
   cd ntree
   ```

2. Set up the database:
   ```bash
   python makedatabase.py
   ```

3. (Optional) Create an alias for easier access:

   **Linux/macOS**:
   Add to your `~/.bashrc` or `~/.zshrc`:
   ```bash
   alias diary='python /path/to/ntree/main.py'
   ```

   **Windows**:
   Create a batch file `diary.bat` in a directory in your PATH:
   ```batch
   @echo off
   python C:\path\to\ntree\main.py %*
   ```

## Usage

### Basic Commands

```bash
# Show help
diary -h

# Create new entry
diary -n "Had a great meeting today!"

# Show today's entries
diary -t

# Show entries for a specific date
diary -d 2024-01-15

# List all entries (latest 100)
diary -l
```

### Advanced Features

```bash
# Search entries
diary --search "meeting"

# Mark last entry as favorite
diary --fav

# List favorite entries
diary --list-fav

# Nostalgia mode (show all entries with delay)
diary --nostalgia
# With custom delay (in seconds)
diary --nostalgia 1.5
```

## Data Storage

All entries are stored in an SQLite database (`entries.db`) in the same directory as the script. The database is automatically created when you run `makedatabase.py`.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

