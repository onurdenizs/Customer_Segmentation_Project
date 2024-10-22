# correlation_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

DPI_VALUE = 900  # For heatmap image resolution

def calculate_correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the correlation matrix of a DataFrame.
    """
    return df.corr()

def plot_correlation_heatmap(correlation_matrix: pd.DataFrame, output_file: str) -> None:
    """
    Plot and save the correlation matrix heatmap.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(output_file, dpi=DPI_VALUE)
    plt.show()
