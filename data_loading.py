import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    print("Dataset loaded successfully. Shape:", df.shape)
    return df
