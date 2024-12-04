import pandas as pd


def load_dataset(file_path):
    try:
        data = pd.read_csv(file_path)
        print(data.head())
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None


file_path = "uscities.csv"  
cities_data = load_dataset(file_path)
if cities_data is None:
    print("Dataset failed to load.")
else:
    print("Dataset loaded successfully.")




