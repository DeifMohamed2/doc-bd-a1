import pandas as pd

def explore_data(data):
    # Insight 1: Calculate the number of unique values in each column
    unique_values = data.nunique()
    with open('eda-in-1.txt', 'w') as f:
        f.write(f'Number of unique values in each column:\n{unique_values}')

    # Insight 2: Calculate the mean, median, and standard deviation of each numerical column
    numerical_columns = data.select_dtypes(include=['int64', 'float64'])
    statistics = numerical_columns.describe().loc[['mean', '50%', 'std']]
    statistics.rename(index={'50%': 'median'}, inplace=True)  # Rename '50%' to 'median'
    with open('eda-in-2.txt', 'w') as f:
        f.write(f'Descriptive statistics of numerical columns:\n{statistics}')

    # Insight 3: Calculate the correlation between each pair of numerical columns
    correlations = numerical_columns.corr()
    with open('eda-in-3.txt', 'w') as f:
        f.write(f'Correlation matrix:\n{correlations}')

if __name__ == "__main__":
    # Load dataset
    df = pd.read_csv("dataset.csv")

    # Explore data
    explore_data(df)
