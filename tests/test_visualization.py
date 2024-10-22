import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pandas as pd
from scripts.visualization import plot_histogram, plot_scatter
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend for testing


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

def test_plot_histogram(mock_df, tmpdir):
    """Test plotting histogram."""
    output_file = tmpdir.join('age_distribution.jpeg')
    plot_histogram(mock_df, 'Age', 'Age Distribution', 'Age', str(output_file))
    assert output_file.check(), "Histogram was not saved"

def test_plot_scatter(mock_df, tmpdir):
    """Test plotting scatter plot."""
    output_file = tmpdir.join('income_vs_spending.jpeg')
    plot_scatter(mock_df, 'Annual Income (k$)', 'Spending Score (1-100)', 
                 'Annual Income vs Spending Score', 'Annual Income (k$)', 'Spending Score (1-100)', str(output_file))
    assert output_file.check(), "Scatter plot was not saved"
