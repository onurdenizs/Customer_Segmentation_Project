from scripts.data_preprocessing import handle_missing_values, encode_categorical, load_data
from scripts.correlation_analysis import calculate_correlation_matrix, plot_correlation_heatmap
from scripts.visualization import plot_histogram, plot_scatter
from scripts.feature_selection import select_features

DATA_PATH = 'data/raw/Mall_Customers.csv'

def main():
    # Load the dataset
    df = load_data(DATA_PATH)

    # Handle missing values
    df = handle_missing_values(df, strategy='drop')

    # Encode categorical variables (e.g., 'Genre')
    df = encode_categorical(df, 'Genre')

    # Calculate the correlation matrix
    correlation_matrix = calculate_correlation_matrix(df)

    # Select features based on correlation with the target column
    selected_features = select_features(correlation_matrix, target_column='Spending Score (1-100)')

    # Plot the correlation heatmap for selected features
    plot_correlation_heatmap(correlation_matrix, 'correlation_heatmap.jpeg')

    # Plot histograms and scatter plots as needed
    if 'Age' in selected_features.columns:
        plot_histogram(selected_features, 'Age', 'Age Distribution', 'Age', 'age_distribution.jpeg')
    else:
        plot_histogram(df, 'Age', 'Age Distribution', 'Age', 'age_distribution.jpeg')

    if 'Annual Income (k$)' in selected_features.columns:
        plot_histogram(selected_features, 'Annual Income (k$)', 'Annual Income Distribution', 'Annual Income (k$)', 'annual_income_distribution.jpeg')
    else:
        plot_histogram(df, 'Annual Income (k$)', 'Annual Income Distribution', 'Annual Income (k$)', 'annual_income_distribution.jpeg')

    if 'Annual Income (k$)' in selected_features.columns and 'Spending Score (1-100)' in selected_features.columns:
        plot_scatter(selected_features, 'Annual Income (k$)', 'Spending Score (1-100)', 
                     'Annual Income vs Spending Score', 'Annual Income (k$)', 
                     'Spending Score (1-100)', 'annual_income_vs_spending_score.jpeg')
    else:
        plot_scatter(df, 'Annual Income (k$)', 'Spending Score (1-100)', 
                     'Annual Income vs Spending Score', 'Annual Income (k$)', 
                     'Spending Score (1-100)', 'annual_income_vs_spending_score.jpeg')

if __name__ == "__main__":
    main()
