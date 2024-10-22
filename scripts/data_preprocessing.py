# data_preprocessing.py

import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads a dataset from a CSV file.

    Args:
        file_path (str): The path to the dataset file.

    Returns:
        pd.DataFrame: A DataFrame containing the loaded dataset.

    Raises:
        FileNotFoundError: If the file does not exist at the provided path.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file cannot be parsed into a DataFrame.
    """
    return pd.read_csv(file_path)


def handle_missing_values(df: pd.DataFrame, strategy: str = 'drop', fill_value: any = None) -> pd.DataFrame:
    """
    Handles missing values in the DataFrame according to the specified strategy.

    Args:
        df (pd.DataFrame): DataFrame containing the dataset.
        strategy (str, optional): Strategy to handle missing values.
            - 'drop': Drops rows with missing values (default).
            - 'fill': Fills missing values with `fill_value`.
        fill_value (any, optional): Value to fill missing values with, required if `strategy='fill'`. Default is None.

    Returns:
        pd.DataFrame: DataFrame with missing values handled.

    Raises:
        ValueError: If `strategy` is not 'drop' or 'fill', or if `strategy` is 'fill' and `fill_value` is not provided.
    """
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'fill' and fill_value is not None:
        return df.fillna(fill_value)
    else:
        raise ValueError("Invalid strategy. Choose either 'drop' or 'fill' and provide a fill_value if filling.")


def encode_categorical(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Encodes a categorical variable using one-hot encoding.

    Args:
        df (pd.DataFrame): DataFrame containing the dataset.
        column (str): The name of the column to encode.

    Returns:
        pd.DataFrame: DataFrame with the specified categorical column encoded using one-hot encoding.

    Raises:
        KeyError: If the specified column does not exist in the DataFrame.
    """
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found in DataFrame.")
    return pd.get_dummies(df, columns=[column], drop_first=False)


def handle_outliers(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Handles outliers in the specified columns using the Interquartile Range (IQR) method.

    Args:
        df (pd.DataFrame): DataFrame containing the dataset.
        columns (list): List of column names in which to handle outliers.

    Returns:
        pd.DataFrame: DataFrame with outliers removed.

    Raises:
        KeyError: If any of the specified columns are not found in the DataFrame.
        ValueError: If any column in the list is not numerical.
    """
    for column in columns:
        if column not in df.columns:
            raise KeyError(f"Column '{column}' not found in DataFrame.")
        if not pd.api.types.is_numeric_dtype(df[column]):
            raise ValueError(f"Column '{column}' must be numerical to detect outliers.")
        
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    
    return df
