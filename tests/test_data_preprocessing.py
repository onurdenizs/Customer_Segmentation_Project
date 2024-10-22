import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pandas as pd
from scripts.data_preprocessing import load_data, handle_missing_values, encode_categorical, handle_outliers

# Mock data for testing
@pytest.fixture
def mock_df():
    data = {
        'CustomerID': [1, 2, 3, 4, 5],
        'Age': [19, 21, 20, 23, 31],
        'Annual Income (k$)': [15, 16, 17, 18, 19],
        'Spending Score (1-100)': [39, 81, 6, 77, 40]
    }
    return pd.DataFrame(data)

def test_load_data():
    """Test that data is loaded correctly."""
    df = load_data('data/raw/Mall_Customers.csv')
    assert isinstance(df, pd.DataFrame), "Loaded data is not a DataFrame"
    assert df.shape[0] > 0, "Loaded DataFrame is empty"

def test_handle_missing_values_drop(mock_df):
    """Test dropping missing values."""
    df = mock_df.copy()
    df.loc[0, 'Age'] = None
    cleaned_df = handle_missing_values(df, strategy='drop')
    assert cleaned_df.shape[0] == 4, "Row with missing value was not dropped"

def test_handle_missing_values_fill(mock_df):
    """Test filling missing values."""
    df = mock_df.copy()
    df.loc[0, 'Age'] = None
    cleaned_df = handle_missing_values(df, strategy='fill', fill_value=25)
    assert cleaned_df.loc[0, 'Age'] == 25, "Missing value was not filled correctly"

def test_encode_categorical(mock_df):
    """Test encoding categorical variables."""
    df = mock_df.copy()
    df['Gender'] = ['Male', 'Female', 'Female', 'Male', 'Male']
    encoded_df = encode_categorical(df, 'Gender')
    assert 'Gender_Female' in encoded_df.columns, "Categorical encoding failed"

def test_handle_outliers(mock_df):
    """Test handling outliers."""
    df = mock_df.copy()
    df.loc[0, 'Annual Income (k$)'] = 100  # Add an outlier
    cleaned_df = handle_outliers(df, ['Annual Income (k$)'])
    assert cleaned_df.shape[0] == 4, "Outlier was not handled correctly"
