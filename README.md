# 🎓 Student Performance Analyzer

This project applies data analytics and visualization techniques to explore and understand key factors affecting student academic performance.

## 📁 Project Structure
├── main.py # Runs full preprocessing and saves cleaned data
├── data_loading.py # Handles data import
├── preprocessing.py # Cleans, transforms, and encodes data
├── visualisations.py # Contains reusable plotting functions
├── final_visualizations.ipynb # 📊 Main notebook for visual storytelling
├── student_performance_data.csv # 📂 Dataset used
└── README.md # 📘 You're here!

## 📊 Key Visualizations
-------------------------------------------------------------
|          Insight                    |    Chart Type       |
|-------------------------------------|---------------------|
| Performance Level Distribution      | Bar Plot            |
| GPA, Attendance, Study Hours Spread | Boxplot             |
| Study Hours vs GPA                  | Interactive Scatter |
| GPA by Gender                       | KDE Histogram       |
| Feature Relationships               | Correlation Heatmap |
-------------------------------------------------------------
## 📈 Tools Used

- Python
- Pandas
- Seaborn
- Matplotlib
- Plotly
- Jupyter Notebook
- VS Code

## 📘 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Rishankgupta08/Student-Performance-Analyzer.git
Install required libraries:

pip install pandas matplotlib seaborn plotly
Open final_visualizations.ipynb in Jupyter or VS Code.

Run all cells to explore visual insights.

📌 Dataset Info
The dataset includes attributes like Gender, Age, StudyHoursPerWeek, AttendanceRate, GPA, Major, PartTimeJob, and ExtraCurricularActivities.

GPA-based performance levels were derived and used for visualization and analysis.

✅ Outcome
This project helps identify trends, outliers, and correlations that can guide educational strategies and interventions to improve student performance.

🙌 Credits
Dataset: Kaggle – Student Habits & Academic Performance Dataset.
