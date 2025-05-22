import pandas as pd

def handle_missing_values(df):
    missing = df.isnull().sum()
    print("Missing values per column:\n", missing)
    # Fill missing values: mode for categorical, median for numeric
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype == 'O':  # Object means categorical
                df[col].fillna(df[col].mode()[0], inplace=True)
            else:
                df[col].fillna(df[col].median(), inplace=True)
    print("Missing values handled.")
    return df

def feature_engineering(df):
    # Create average score
    df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
    
    # Categorize performance level based on average score
    bins = [0, 60, 80, 100]
    labels = ['Low', 'Average', 'High']
    df['performance_level'] = pd.cut(df['average_score'], bins=bins, labels=labels)
    
    print("Feature engineering done.")
    return df

def encode_features(df):
    # One-hot encode categorical columns
    df_encoded = pd.get_dummies(df, columns=['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course'], drop_first=True)
    print("Categorical features encoded.")
    return df_encoded
