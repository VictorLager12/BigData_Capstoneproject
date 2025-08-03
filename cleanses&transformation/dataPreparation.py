import pandas as pd
import numpy as np

# Read the uploaded CSV file
df = pd.read_csv('cfa_cleaned.csv')

# Step 1: Drop rows with missing 'Lat' or 'Long' values
df_cleaned = df.dropna(subset=['Lat', 'Long']).copy()

# Step 2: Fill missing 'Ownership' values with 'Unknown'
df_cleaned['Ownership'] = df_cleaned['Ownership'].fillna('Unknown')

# Step 3: Strip leading/trailing whitespace from all string columns
for column in df_cleaned.columns:
    if df_cleaned[column].dtype == 'object':
        df_cleaned[column] = df_cleaned[column].str.strip()

# Display the information of the cleaned DataFrame to verify the changes
print("Information for the fully cleaned DataFrame:")
print(df_cleaned.info())

# Display missing values in the cleaned DataFrame to confirm they have been handled
print("\nMissing values in the fully cleaned DataFrame:")
print(df_cleaned.isnull().sum())

# Save the fully cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cfa_fully_cleaned.csv', index=False)