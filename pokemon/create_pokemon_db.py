import pandas as pd
import sqlite3
import os

# Define the path to the dataset
dataset_path = r'C:\Users\laure\ds3500\ds3500_mini_project\pokemon_dashboard\pokemon\pokemon.csv'

# Load the dataset
df = pd.read_csv(dataset_path)

# Define where to save the SQLite database
db_path = r'C:\Users\laure\ds3500\ds3500_mini_project\pokemon_dashboard\pokemon.db'

# Connect to SQLite database (or create it)
conn = sqlite3.connect(db_path)

# Save the DataFrame to the SQLite database
df.to_sql('pokemon', conn, if_exists='replace', index=False)

# Create indexes with properly quoted column names
conn.execute('CREATE INDEX IF NOT EXISTS idx_name ON pokemon (Name)')
conn.execute('CREATE INDEX IF NOT EXISTS idx_type1 ON pokemon ("Type 1")')
conn.execute('CREATE INDEX IF NOT EXISTS idx_type2 ON pokemon ("Type 2")')

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"SQLite database created successfully at: {db_path}")
