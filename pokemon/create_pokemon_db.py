import pandas as pd
import sqlite3
import os

# Define the path to the dataset
dataset_path = r'pokemon.csv'

# Load the dataset
df = pd.read_csv(dataset_path)

# Define where to save the SQLite database
db_path = r'pokemon.db'

# Connect to SQLite database (or create it)
conn = sqlite3.connect(db_path)

# Save the DataFrame to the SQLite database
df.to_sql('pokemon', conn, if_exists='replace', index=False)

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


print(f"SQLite database created successfully at: {db_path}")





