import matplotlib.pyplot as plt
import seaborn as sns

def plot_performance_level(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(x='performance_level', data=df, palette='viridis')
    plt.title('Performance Level Distribution')
    plt.show()

def plot_scores_boxplot(df):
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=df[['GPA', 'StudyHoursPerWeek', 'AttendanceRate']])
    plt.title('Boxplot of GPA, Study Hours, and Attendance')
    plt.show()

def plot_correlation_matrix(df):
    plt.figure(figsize=(8, 6))
    sns.heatmap(df[['GPA', 'StudyHoursPerWeek', 'AttendanceRate', 'Study_Attendance_Ratio']].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

def plot_score_distribution_by_gender(df):
    plt.figure(figsize=(10, 4))
    sns.histplot(data=df, x='GPA', hue='Gender', kde=True, palette='Set1', bins=20)
    plt.title('GPA Distribution by Gender')
    plt.show()
