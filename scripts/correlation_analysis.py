# correlation_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

DPI_VALUE = 900  # For heatmap image resolution

def calculate_correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the correlation matrix of a DataFrame.

    This function computes the pairwise correlation between the columns of a DataFrame. 
    The correlation values range between -1 and 1, where:
        - 1 indicates a perfect positive correlation
        - -1 indicates a perfect negative correlation
        - 0 indicates no correlation
    
    Args:
        df (pd.DataFrame): DataFrame containing the data for which correlations are to be calculated.

    Returns:
        pd.DataFrame: A DataFrame containing the correlation matrix, where each value represents 
        the correlation between two columns in the input DataFrame.
    """
    return df.corr()

def plot_correlation_heatmap(correlation_matrix: pd.DataFrame, output_file: str) -> None:
    """
    Plot and save the correlation matrix heatmap.

    This function creates a heatmap visualization of the correlation matrix. 
    The heatmap is color-coded to indicate the strength and direction of correlations.
    The resulting image is saved to the specified file location.

    Args:
        correlation_matrix (pd.DataFrame): The correlation matrix (as a DataFrame) to visualize.
        output_file (str): The file path (including the filename and extension) where the heatmap image will be saved.

    Returns:
        None: The function saves the heatmap as an image and displays it.

    Example:
        correlation_matrix = calculate_correlation_matrix(df)
        plot_correlation_heatmap(correlation_matrix, 'path/to/save/heatmap.jpeg')
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(output_file, dpi=DPI_VALUE)
    plt.show()
