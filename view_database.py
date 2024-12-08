import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Execute a query to fetch all records from the users table
cursor.execute("SELECT * FROM users")

# Fetch all rows
users = cursor.fetchall()

# Print the records
for user in users:
    print(user)

# Close the connection
conn.close()
