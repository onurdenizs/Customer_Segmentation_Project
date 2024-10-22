# data_preprocessing.py

import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load dataset from a CSV file.
    
    Args:
        file_path (str): The path to the dataset file.
    
    Returns:
        pd.DataFrame: DataFrame containing the loaded dataset.
    """
    return pd.read_csv(file_path)

def handle_missing_values(df: pd.DataFrame, strategy='drop', fill_value=None) -> pd.DataFrame:
    """
    Handle missing values in the dataset.
    """
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'fill' and fill_value is not None:
        return df.fillna(fill_value)
    else:
        raise ValueError("Invalid strategy. Choose either 'drop' or 'fill' and provide a fill_value if filling.")

def encode_categorical(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Encode a categorical variable using one-hot encoding.
    """
    return pd.get_dummies(df, columns=[column], drop_first=False)

def handle_outliers(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Handle outliers in the specified columns using the IQR method.
    """
    for column in columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df
