# feature_selection.py

import pandas as pd
from scripts.correlation_analysis import calculate_correlation_matrix

def select_features(df: pd.DataFrame, target_column: str, method: str = 'correlation', threshold: float = 0.5) -> pd.DataFrame:
    """
    Select relevant features based on the specified method.

    Args:
        df (pd.DataFrame): The input DataFrame containing the features.
        target_column (str): The target column for feature selection.
        method (str): The method for feature selection ('correlation' or others).
        threshold (float): The threshold for selecting features (for correlation method).

    Returns:
        pd.DataFrame: DataFrame containing selected features.
    """
    if method == 'correlation':
        # Calculate the correlation matrix using an existing function
        corr_matrix = calculate_correlation_matrix(df)

        # Get the correlations for the target column
        correlations_with_target = corr_matrix[target_column].abs()

        # Select features that have correlation with the target greater than the threshold
        selected_features = correlations_with_target[correlations_with_target > threshold].index

        # Return the DataFrame with the selected features
        return df[selected_features]
    else:
        raise ValueError("Unsupported method. Currently only 'correlation' is implemented.")
