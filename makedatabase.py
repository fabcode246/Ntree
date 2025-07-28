import sqlite3

def setup_database(db_path: str = "entries.db") -> None:
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Drop existing table if it exists
        cursor.execute("DROP TABLE IF EXISTS entry")

        # Create table with proper constraints
        cursor.execute("""
        CREATE TABLE entry (
            content TEXT NOT NULL,
            id TEXT NOT NULL,
            d TEXT NOT NULL,
            t TEXT NOT NULL,
            fav INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY (id)
        )
        """)

        # Create indexes for better query performance
        cursor.execute("CREATE INDEX idx_date ON entry(d)")
        cursor.execute("CREATE INDEX idx_fav ON entry(fav)")
        cursor.execute("CREATE INDEX idx_content ON entry(content)")

        conn.commit()
        print("Database setup completed successfully!")

    except sqlite3.Error as e:
        print(f"Error setting up database: {e}")

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    setup_database()
