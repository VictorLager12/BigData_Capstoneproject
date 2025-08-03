import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the cleaned dataset
df = pd.read_csv('cfa_fully_cleaned.csv')

# Generate descriptive statistics for numerical columns
print("Descriptive Statistics for Numerical Columns:")
print(df.describe())

# Generate descriptive statistics for categorical columns
print("\nDescriptive Statistics for Categorical Columns:")
print(df.describe(include='object'))

# Check value counts for categorical columns to get a better sense of distribution
print("\nValue Counts for 'Country' column:")
print(df['Country'].value_counts())

print("\nValue Counts for 'Facility type' column (top 20):")
print(df['Facility type'].value_counts().head(20))

print("\nValue Counts for 'Ownership' column:")
print(df['Ownership'].value_counts())

print("\nValue Counts for 'LL source' column:")
print(df['LL source'].value_counts())

# Set a style for the plots
sns.set_style("whitegrid")

# --- Visualization 1: Distribution of Facilities by Country ---
plt.figure(figsize=(12, 8))
country_counts = df['Country'].value_counts().head(20) # Top 20 countries for readability
sns.barplot(x=country_counts.values, y=country_counts.index, palette='viridis')
plt.title('Top 20 Countries by Number of Health Facilities', fontsize=16)
plt.xlabel('Number of Facilities', fontsize=12)
plt.ylabel('Country', fontsize=12)
plt.tight_layout()
plt.savefig('top_20_countries_facilities.png') # Save the plot as PNG
plt.show()

print("Description: This bar plot displays the top 20 countries with the highest number of health facilities. It helps identify which countries are most represented in the dataset and potentially where health infrastructure is more concentrated or better documented.")

# --- Visualization 2: Distribution of Facility Types ---
plt.figure(figsize=(12, 8))
facility_type_counts = df['Facility type'].value_counts().head(20) # Top 20 facility types
sns.barplot(x=facility_type_counts.values, y=facility_type_counts.index, palette='magma')
plt.title('Top 20 Facility Types by Count', fontsize=16)
plt.xlabel('Number of Facilities', fontsize=12)
plt.ylabel('Facility Type', fontsize=12)
plt.tight_layout()
plt.savefig('top_20_facility_types.png') # Save the plot as PNG
plt.show()

print("Description: This bar plot shows the distribution of the top 20 most common facility types. It provides insight into the predominant types of health service points available across the African countries in the dataset, such as clinics, dispensaries, and health centers.")

# --- Visualization 3: Distribution of Ownership Types ---
plt.figure(figsize=(10, 7))
ownership_counts = df['Ownership'].value_counts()
sns.barplot(x=ownership_counts.values, y=ownership_counts.index, palette='cividis')
plt.title('Distribution of Health Facility Ownership Types', fontsize=16)
plt.xlabel('Number of Facilities', fontsize=12)
plt.ylabel('Ownership Type', fontsize=12)
plt.tight_layout()
plt.savefig('ownership_distribution.png') # Save the plot as PNG
plt.show()

print("Description: This bar plot illustrates the distribution of different ownership types for health facilities. It highlights the prevalence of government (MoH, Public, Publique) and 'Unknown' ownership, as well as the contributions of other entities like FBOs, NGOs, and private organizations.")

# --- Visualization 4: Geographical Distribution of Facilities (Scatter Plot) ---
plt.figure(figsize=(15, 10))
sns.scatterplot(x='Long', y='Lat', data=df, hue='LL source', s=10, alpha=0.6, palette='tab10')
plt.title('Geographical Distribution of Health Facilities Across Africa', fontsize=16)
plt.xlabel('Longitude', fontsize=12)
plt.ylabel('Latitude', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='LL Source', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('geographical_distribution.png') # Save the plot as PNG
plt.show()

print("Description: This scatter plot visualizes the geographical spread of health facilities using their latitude and longitude coordinates. Each point represents a facility, and points are colored by their 'LL source' to show how different data sources contribute to the geographical coverage. It helps identify regions with higher or lower concentrations of facilities.")

# --- Visualization 5: Top Facility Types by Ownership (Heatmap) ---
# Create a crosstab for Facility Type and Ownership, then select top N types and owners
top_facility_types = df['Facility type'].value_counts().head(10).index
top_ownership_types = df['Ownership'].value_counts().head(10).index

# Filter the DataFrame to include only these top types/owners
df_filtered = df[df['Facility type'].isin(top_facility_types) & df['Ownership'].isin(top_ownership_types)]

# Create the pivot table
pivot_table = pd.crosstab(df_filtered['Facility type'], df_filtered['Ownership'])

plt.figure(figsize=(14, 10))
sns.heatmap(pivot_table, annot=True, fmt='d', cmap='YlGnBu', linewidths=.5)
plt.title('Relationship Between Top 10 Facility Types and Top 10 Ownership Types', fontsize=16)
plt.xlabel('Ownership Type', fontsize=12)
plt.ylabel('Facility Type', fontsize=12)
plt.tight_layout()
plt.savefig('facility_type_ownership_heatmap.png') # Save the plot as PNG
plt.show()

print("Description: This heatmap illustrates the relationship between the top 10 most common facility types and the top 10 ownership types. The color intensity and annotated numbers indicate the count of facilities for each combination, revealing which ownership entities are most prevalent for specific facility types.")
