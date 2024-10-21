# scripts/data_exploration.py

import pandas as pd

# Define the path to the dataset
data_path = "data/raw/Mall_Customers.csv"

# Step 1: Import the dataset
df = pd.read_csv(data_path)

# Step 2: Display the first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: Check the dataset information
print("\nDataset Information:")
print(df.info())

# Step 4: Check for missing values
print("\nMissing Values in the Dataset:")
print(df.isnull().sum())

# Step 5: Display descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())
