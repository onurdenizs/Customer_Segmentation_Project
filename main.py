# main.py

from scripts.data_preprocessing import handle_missing_values, encode_categorical
from scripts.correlation_analysis import calculate_correlation_matrix, plot_correlation_heatmap
from scripts.visualization import plot_histogram, plot_scatter

import pandas as pd

DATA_PATH = "data/raw/Mall_Customers.csv"

def main():
    # Load the dataset
    df = pd.read_csv(DATA_PATH)

    # Handle missing values
    df = handle_missing_values(df, strategy='drop')

    # Encode categorical variables (e.g., 'Genre')
    df = encode_categorical(df, 'Genre')

    # Analyze correlations
    correlation_matrix = calculate_correlation_matrix(df)

    # Visualize the correlation heatmap
    plot_correlation_heatmap(correlation_matrix, 'correlation_heatmap.jpeg')

    # Visualize distributions and scatter plots
    plot_histogram(df, 'Age', 'Age Distribution', 'Age', 'age_distribution.jpeg')
    plot_histogram(df, 'Annual Income (k$)', 'Annual Income Distribution', 'Annual Income (k$)', 'annual_income_distribution.jpeg')
    plot_scatter(df, 'Annual Income (k$)', 'Spending Score (1-100)', 'Annual Income vs Spending Score', 'Annual Income (k$)', 'Spending Score (1-100)', 'annual_income_vs_spending_score.jpeg')

if __name__ == "__main__":
    main()
