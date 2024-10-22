import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pandas as pd
from scripts.correlation_analysis import calculate_correlation_matrix, plot_correlation_heatmap

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

def test_calculate_correlation_matrix(mock_df):
    """Test calculation of correlation matrix."""
    corr_matrix = calculate_correlation_matrix(mock_df)
    assert isinstance(corr_matrix, pd.DataFrame), "Correlation matrix is not a DataFrame"
    assert corr_matrix.shape[0] == 4, "Correlation matrix shape is incorrect"

def test_plot_correlation_heatmap(mock_df, tmpdir):
    """Test plotting the correlation heatmap."""
    corr_matrix = calculate_correlation_matrix(mock_df)
    output_file = tmpdir.join('correlation_heatmap.jpeg')
    plot_correlation_heatmap(corr_matrix, str(output_file))
    assert output_file.check(), "Heatmap was not saved"
