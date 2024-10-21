# tests/test_data_exploration.py

import pytest
import pandas as pd
import os

# Define the path to the dataset
DATA_PATH = "data/raw/Mall_Customers.csv"

# Test 1: Ensure the dataset loads correctly
def test_load_data():
    """Test if the CSV file loads correctly into a pandas DataFrame."""
    assert os.path.exists(DATA_PATH), f"{DATA_PATH} does not exist."
    
    df = pd.read_csv(DATA_PATH)
    assert isinstance(df, pd.DataFrame), "Loaded data is not a DataFrame."

# Test 2: Ensure the dataset has the correct number of rows and columns
def test_data_shape():
    """Test if the dataset has the expected shape (200 rows, 5 columns)."""
    df = pd.read_csv(DATA_PATH)
    assert df.shape == (200, 5), f"Dataset shape is incorrect, got {df.shape}"

# Test 3: Ensure the data types are as expected
def test_data_types():
    """Test if the dataset columns have the correct data types."""
    df = pd.read_csv(DATA_PATH)
    expected_dtypes = {
        'CustomerID': 'int64',
        'Genre': 'object',
        'Age': 'int64',
        'Annual Income (k$)': 'int64',
        'Spending Score (1-100)': 'int64'
    }
    actual_dtypes = df.dtypes.to_dict()

    for column, expected_dtype in expected_dtypes.items():
        assert str(actual_dtypes[column]) == expected_dtype, f"Incorrect dtype for {column}"

# Test 4: Ensure there are no missing values
def test_missing_values():
    """Test if the dataset has any missing values."""
    df = pd.read_csv(DATA_PATH)
    assert df.isnull().sum().sum() == 0, "There are missing values in the dataset."
