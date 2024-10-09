import sqlite3

# Path to the SQLite database
db_path = r'C:\Users\laure\ds3500\ds3500_mini_project\pokemon_dashboard\pokemon.db'

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Example query: Get all Pokémon of Fire type
query = 'SELECT * FROM pokemon WHERE "Type 1" = "Fire"'
cursor.execute(query)

# Fetch and print results
fire_pokemon = cursor.fetchall()
for pokemon in fire_pokemon:
    print(pokemon)

# Close the connection
conn.close()
