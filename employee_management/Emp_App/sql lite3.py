import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Execute a SQL query
cursor.execute("SELECT * FROM employees")

# Fetch the results
results = cursor.fetchall()

# Close the database connection
conn.close()
