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
        # Reusing the calculate_correlation_matrix function instead of df.corr()
        corr_matrix = calculate_correlation_matrix(df)
        high_corr = corr_matrix[target_column][corr_matrix[target_column].abs() > threshold].index
        return df[high_corr]
    else:
        raise ValueError("Unsupported method. Currently only 'correlation' is implemented.")
