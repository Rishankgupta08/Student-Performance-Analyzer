import matplotlib.pyplot as plt
import seaborn as sns

def plot_performance_level(df):
    plt.figure(figsize=(6,4))
    sns.countplot(x='performance_level', data=df, palette='viridis')
    plt.title('Student Performance Level Distribution')
    plt.show()

def plot_scores_boxplot(df):
    plt.figure(figsize=(12,5))
    sns.boxplot(data=df[['math score', 'reading score', 'writing score']])
    plt.title('Boxplot of Scores')
    plt.show()

def plot_correlation_matrix(df):
    plt.figure(figsize=(8,6))
    sns.heatmap(df[['math score', 'reading score', 'writing score', 'average_score']].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

def plot_score_distribution_by_gender(df):
    plt.figure(figsize=(12,4))
    sns.histplot(data=df, x='math score', hue='gender', kde=True, palette='Set1', bins=20)
    plt.title('Math Score Distribution by Gender')
    plt.show()
