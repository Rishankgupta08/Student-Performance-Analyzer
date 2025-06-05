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
    # Categorize GPA into performance levels
    bins = [0, 2.5, 3.5, 4.1]
    labels = ['Low', 'Average', 'High']
    df['performance_level'] = pd.cut(df['GPA'], bins=bins, labels=labels)

    # Create a derived column: study-to-attendance ratio
    df['Study_Attendance_Ratio'] = df['StudyHoursPerWeek'] / (df['AttendanceRate'] + 1)

    # Convert Yes/No to binary
    df['PartTimeJob'] = df['PartTimeJob'].apply(lambda x: 1 if x == 'Yes' else 0)
    df['ExtraCurricularActivities'] = df['ExtraCurricularActivities'].apply(lambda x: 1 if x == 'Yes' else 0)

    print("Feature engineering done.")
    return df


def encode_features(df):
    # One-hot encode only the valid categorical columns in your dataset
    df_encoded = pd.get_dummies(df, columns=['Gender', 'Major'], drop_first=True)
    print("Categorical features encoded.")
    return df_encoded
