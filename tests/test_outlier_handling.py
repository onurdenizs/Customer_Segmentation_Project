# tests/test_outlier_handling.py

import pandas as pd
from scripts.data_exploration import handle_outliers

def test_handle_outliers():
    # Create a small sample dataframe with outliers
    data = {'Age': [22, 25, 26, 30, 29, 120],  # 120 is an outlier
            'Annual Income (k$)': [15, 16, 18, 20, 17, 200]}  # 200 is an outlier
    df = pd.DataFrame(data)
    
    # Use IQR method to handle outliers
    cleaned_df = handle_outliers(df, ['Age', 'Annual Income (k$)'])
    
    # Check that outliers are removed
    assert cleaned_df['Age'].max() <= 100  # Assuming 100 is a reasonable upper limit for Age
    assert cleaned_df['Annual Income (k$)'].max() <= 100  # Assuming 100 is a reasonable upper limit for Income
