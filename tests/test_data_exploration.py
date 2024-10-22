import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pandas as pd
from scripts.data_exploration import load_data, display_basic_info

import pytest
import pandas as pd
from scripts.data_exploration import load_data, display_basic_info

# Mock DataFrame for testing
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
    """Test that the data is loaded correctly."""
    df = load_data('data/raw/Mall_Customers.csv')
    assert isinstance(df, pd.DataFrame), "Loaded data is not a DataFrame"
    assert df.shape[0] > 0, "Loaded DataFrame is empty"

def test_display_basic_info(mock_df, capsys):
    """Test that basic information is displayed correctly."""
    display_basic_info(mock_df)
    
    captured = capsys.readouterr()
    assert "First 5 rows of the dataset" in captured.out
    assert "Dataset Information" in captured.out
    assert "Missing Values in the Dataset" in captured.out
    assert "Descriptive Statistics" in captured.out

# Additional tests for plotting functions can be added similarly

