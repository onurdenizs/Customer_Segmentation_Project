"""" 
data_exploration.py

This script performs basic exploratory data analysis (EDA) on the Mall Customers dataset.
It imports the data, displays key information, and visualizes distributions and relationships
within the dataset. The figures are saved as high-resolution images for reporting.

Author: Onur Deniz
Date: 21.10.2024
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Constants
DATA_PATH = "data/raw/Mall_Customers.csv"  # Path to the raw data file
SAVE_DIR = 'reports/figures/'  # Directory to save output figures
DPI_VALUE = 900  # High-resolution for saved images (DPI)

def handle_missing_values(df: pd.DataFrame, strategy='drop', fill_value=None) -> pd.DataFrame:
    """
    Handle missing values in the dataset.
    
    Args:
        df (pd.DataFrame): DataFrame containing the dataset.
        strategy (str): Strategy to handle missing values ('drop' to drop rows with missing values,
                        'fill' to fill missing values).
        fill_value (any): Value to fill missing values with, if strategy is 'fill'.
        
    Returns:
        pd.DataFrame: DataFrame with missing values handled.
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

    Args:
        df (pd.DataFrame): DataFrame containing the dataset.
        column (str): The column to encode.

    Returns:
        pd.DataFrame: DataFrame with the categorical column encoded.
    """
    return pd.get_dummies(df, columns=[column], drop_first=False)


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load dataset from a CSV file.

    Args:
        file_path (str): The path to the dataset file.

    Returns:
        pd.DataFrame: DataFrame containing the loaded dataset.
    """
    return pd.read_csv(file_path)

def display_basic_info(df: pd.DataFrame) -> None:
    """
    Display basic information of the dataset including the first 5 rows, dataset info, 
    missing values, and descriptive statistics.

    Args:
        df (pd.DataFrame): DataFrame containing the dataset.
    """
    print("First 5 rows of the dataset:")
    print(df.head())

    print("\nDataset Information:")
    df.info()

    print("\nMissing Values in the Dataset:")
    print(df.isnull().sum())

    print("\nDescriptive Statistics:")
    print(df.describe())

def save_and_show_plot(fig: plt.Figure, filename: str, save_dir: str, dpi_value: int) -> None:
    """
    Save a figure as an image and display it.

    Args:
        fig (plt.Figure): The figure object to save.
        filename (str): The name of the file to save the figure.
        save_dir (str): The directory to save the figure in.
        dpi_value (int): The resolution of the saved image in DPI.
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    fig.savefig(os.path.join(save_dir, filename), format='jpeg', dpi=dpi_value)
    plt.show()

def plot_histogram(df: pd.DataFrame, column: str, title: str, xlabel: str, filename: str) -> None:
    """
    Plot and save a histogram for a specified column.

    Args:
        df (pd.DataFrame): DataFrame containing the dataset.
        column (str): The column to plot.
        title (str): The title of the plot.
        xlabel (str): The label for the x-axis.
        filename (str): The name of the file to save the plot.
    """
    fig = plt.figure(figsize=(8, 6))
    sns.histplot(df[column], bins=20, kde=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Frequency')
    save_and_show_plot(fig, filename, SAVE_DIR, DPI_VALUE)

def plot_scatter(df: pd.DataFrame, x_col: str, y_col: str, title: str, xlabel: str, ylabel: str, filename: str) -> None:
    """
    Plot and save a scatter plot for two specified columns.

    Args:
        df (pd.DataFrame): DataFrame containing the dataset.
        x_col (str): The column for the x-axis.
        y_col (str): The column for the y-axis.
        title (str): The title of the plot.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.
        filename (str): The name of the file to save the plot.
    """
    fig = plt.figure(figsize=(8, 6))
    sns.scatterplot(x=x_col, y=y_col, data=df)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    save_and_show_plot(fig, filename, SAVE_DIR, DPI_VALUE)

if __name__ == "__main__":
    # Step 1: Load the dataset
    df = load_data(DATA_PATH)

    # Step 2: Handle missing values
    df = handle_missing_values(df, strategy='drop')

    # Step 3: Encode categorical variables (e.g., 'Genre')
    df = encode_categorical(df, 'Genre')

    # Step 4: Display basic info about the dataset
    display_basic_info(df)
    
    # Step 5: Visualize age distribution
    plot_histogram(df, 'Age', 'Age Distribution', 'Age', 'age_distribution.jpeg')

    # Step 6: Visualize annual income distribution
    plot_histogram(df, 'Annual Income (k$)', 'Annual Income Distribution', 'Annual Income (k$)', 'annual_income_distribution.jpeg')

    # Step 7: Scatter plot of Annual Income vs Spending Score
    plot_scatter(df, 'Annual Income (k$)', 'Spending Score (1-100)', 
                 'Annual Income vs Spending Score', 'Annual Income (k$)', 
                 'Spending Score (1-100)', 'annual_income_vs_spending_score.jpeg')
