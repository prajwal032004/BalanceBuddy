import sqlite3

def create_db():
    # Connect to SQLite database (creates 'database.db' if it doesn't exist)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create 'users' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    print("Database and 'users' table created successfully!")

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
