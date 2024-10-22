# tests/test_data_cleaning.py

import pytest
import pandas as pd
from scripts.data_exploration import handle_missing_values  # Placeholder for the function we will implement

def test_handle_missing_values():
    """
    Test to ensure missing values are properly handled by the function.
    """
    # Example dataset with missing values
    data = {
        'CustomerID': [1, 2, None, 4],
        'Genre': ['Male', 'Female', 'Female', None],
        'Age': [23, 35, 45, 29],
        'Annual Income (k$)': [50, None, 85, 40],
        'Spending Score (1-100)': [39, 81, None, 77]
    }
    df = pd.DataFrame(data)

    # Call the function (which we'll implement later)
    clean_df = handle_missing_values(df)

    # Assertions to check the missing values are handled as expected
    assert clean_df.isnull().sum().sum() == 0, "There should be no missing values after handling"
