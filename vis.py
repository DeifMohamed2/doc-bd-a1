import matplotlib.pyplot as plt
import pandas as pd

def visualize_data(df):
    # Your visualization code here
    plt.figure()
    df['Fare'].plot(kind='hist')
    plt.savefig('vis.png')

if __name__ == "__main__":
    # Load dataset
    df = pd.read_csv("dataset.csv")

    # Visualize data
    visualize_data(df)
