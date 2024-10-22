import pytest
import pandas as pd
from scripts.feature_selection import select_features

# Mock DataFrame for testing
@pytest.fixture
def mock_df():
    data = {
        'Feature1': [1, 2, 3, 4, 5],
        'Feature2': [1, 2, 3, 4, 5],  # Perfectly correlated with Feature1
        'Feature3': [5, 4, 3, 2, 1],  # Perfectly negatively correlated with Feature1
        'Feature4': [2, 3, 2, 3, 2],  # Weak correlation with others
        'Target':  [0, 1, 0, 1, 0],  # Target column
    }
    return pd.DataFrame(data)

def test_select_features(mock_df):
    """Test feature selection based on correlation threshold."""
    selected_features = select_features(mock_df, target_column='Target', threshold=0.9)
    
    # Feature1 and Feature2 should be removed as they are highly correlated
    assert selected_features.columns.tolist() == ['Feature1', 'Feature3', 'Feature4', 'Target']

def test_select_features_no_selection(mock_df):
    """Test when no features are selected."""
    selected_features = select_features(mock_df, target_column='Target', threshold=0.99)
    
    # With a high threshold, no features should be removed
    assert selected_features.columns.tolist() == ['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Target']
