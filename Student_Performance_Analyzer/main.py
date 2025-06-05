from data_loading import load_data
from preprocessing import handle_missing_values, feature_engineering, encode_features
from visualisations import plot_performance_level, plot_scores_boxplot, plot_correlation_matrix, plot_score_distribution_by_gender

def main():
    # Load dataset
    df = load_data('Student_performance_data.csv')
    
    # Preprocessing
    df = handle_missing_values(df)
    df = feature_engineering(df)
    
    # EDA visualizations
    plot_performance_level(df)
    plot_scores_boxplot(df)
    plot_correlation_matrix(df)
    plot_score_distribution_by_gender(df)
    
    # Encoding categorical variables
    df_encoded = encode_features(df)
    
    # Save cleaned and encoded dataset
    df_encoded.to_csv('StudentsPerformance_Cleaned.csv', index=False)
    print("Cleaned and encoded dataset saved as 'StudentsPerformance_Cleaned.csv'")

if __name__ == "__main__":
    main()
