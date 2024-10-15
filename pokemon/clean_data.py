# HW 3: Dashboards
# Lauren Cummings & Aarushi Attray
# This is our clean_data.py for cleaning the data we found
# We worked on most parts together, but some were more divided than others

import pandas as pd

dataset_path = r'pokemon.csv'

df = pd.read_csv(dataset_path)
# Mainly done by Lauren
# Lowercase all column names
df.columns = df.columns.str.lower()
# Removing whitespace from 'type 1' and 'type 2'
df.rename(columns={'type 1': 'type1', 'type 2': 'type2'}, inplace=True)
# Changing specified column names (making them lowercase)
df.rename(columns={
    'total': 'overall capabilities',
    'sp. atk': 'special attack',
    'sp. def': 'defensive strength'
}, inplace=True)

print("Cleaned Columns:", df.columns.tolist())
# Filling missing values in 'type2' w/ 'None' to maintain consistency in dataset
df['type2'].fillna('None', inplace=True)
# Replacing NaN values in 'legendary' with False
df['legendary'].fillna(False, inplace=True)  # Replacing NaN with False
# removing duplicates
df.drop_duplicates(inplace=True)
# This just shows the df after cleaning
print("\nCleaned DataFrame:")
print(df.head())
# Saving the cleaned DataFrame to a new CSV file
cleaned_dataset_path = r'cleaned_pokemon.csv'
df.to_csv(cleaned_dataset_path, index=False)
print(f"\nCleaned data saved to: {cleaned_dataset_path}")
