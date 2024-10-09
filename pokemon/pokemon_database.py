import sqlite3

# Path to your SQLite database
db_path = r'C:\Users\laure\ds3500\ds3500_mini_project\pokemon_dashboard\pokemon.db'

# Connect to the database (it will create the database if it doesn't exist)
conn = sqlite3.connect(db_path)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# SQL command to create a table (if it doesn't already exist)
create_table_query = '''
CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type1 TEXT,
    type2 TEXT,
    hp INTEGER,
    attack INTEGER,
    defense INTEGER,
    sp_attack INTEGER,
    sp_defense INTEGER,
    speed INTEGER,
    generation INTEGER,
    legendary BOOLEAN
)
'''

# Execute the SQL command to create the table
cursor.execute(create_table_query)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("Table created successfully!")
