import pandas as pd

# Define the path to the dataset
dataset_path = r'pokemon.csv'

# Load the dataset
df = pd.read_csv(dataset_path)

# Lowercase all column names
df.columns = df.columns.str.lower()

# Remove whitespace from 'type 1' and 'type 2'
df.rename(columns={'type 1': 'type1', 'type 2': 'type2'}, inplace=True)

# Change specified column names
df.rename(columns={
    'total': 'overall capabilities',
    'sp. atk': 'special attack',
    'sp. def': 'defensive strength'
}, inplace=True)

# Display cleaned columns
print("Cleaned Columns:", df.columns.tolist())

# Fill missing values in 'type2' with 'None' for consistency
df['type2'].fillna('None', inplace=True)

# Replace NaN values in 'legendary' with False
df['legendary'].fillna(False, inplace=True)  # Replacing NaN with False

# Remove duplicate entries if any
df.drop_duplicates(inplace=True)

# Display the cleaned DataFrame
print("\nCleaned DataFrame:")
print(df.head())

# Optional: Save the cleaned DataFrame to a new CSV file
cleaned_dataset_path = r'cleaned_pokemon.csv'
df.to_csv(cleaned_dataset_path, index=False)

print(f"\nCleaned data saved to: {cleaned_dataset_path}")
