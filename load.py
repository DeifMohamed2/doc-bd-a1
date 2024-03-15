import pandas as pd
import sys

def load_dataset(file_path):
    # Load dataset
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python load.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    df = load_dataset(file_path)
    if df is not None:
        print("Dataset loaded successfully!")
