import pandas as pd
import logging
from scripts.correlation_analysis import calculate_correlation_matrix

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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
        
        # Log the selected features
        logger.info(f"Selected features based on correlation with '{target_column}' above threshold {threshold}: {list(high_corr)}")
        
        return df[high_corr]
    else:
        # Log an error if an unsupported method is used
        logger.error(f"Unsupported method '{method}' used for feature selection.")
        raise ValueError("Unsupported method. Currently only 'correlation' is implemented.")

if __name__ == "__main__":
    # Example of how to use the logging-enabled feature selection
    df = pd.read_csv('data/raw/Mall_Customers.csv')
    selected_features = select_features(df, target_column='Spending Score (1-100)')
    print(selected_features.head())
