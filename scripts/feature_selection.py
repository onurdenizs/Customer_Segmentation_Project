# feature_selection.py

import pandas as pd

def select_features(correlation_matrix: pd.DataFrame, target_column: str, threshold: float = 0.5) -> pd.DataFrame:
    """
    Select relevant features based on correlation with the target column.

    Args:
        correlation_matrix (pd.DataFrame): The input correlation matrix.
        target_column (str): The target column for feature selection.
        threshold (float): The threshold for selecting features (default is 0.5).

    Returns:
        pd.DataFrame: DataFrame containing selected features.
    """
    high_corr = correlation_matrix.index[correlation_matrix[target_column].abs() > threshold]
    return correlation_matrix[high_corr]
