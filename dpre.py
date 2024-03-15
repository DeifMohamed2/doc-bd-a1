import pandas as pd

def clean_data(data):
  # Remove duplicate rows
  data.drop_duplicates(inplace=True)

  # Remove rows with missing values
  data.dropna(inplace=True)

  # Convert data types
  for column in data.columns:
    if data[column].dtype == 'object':
      data[column] = data[column].astype('category')
    elif data[column].dtype in ['int64', 'float64']:
      data[column] = data[column].astype('float32')


def transform_data(data,feature_name):
  # Create new features
  data[feature_name] = (data[feature_name] - data[feature_name].min()) / (data[feature_name].max() - data[feature_name].min())

  # Feature encoding
  if data[feature_name].dtype == 'category':
    data = pd.get_dummies(data, columns=[feature_name])

def data_Reduction(data):

  # Dimensionality reduction
  data = data.sample(frac=0.5)

  # Feature selection
  data = data.drop(columns=['PassengerId', 'Name'])



def data_discretization(data, bins):
    for column, num_bins in bins.items():
        data[column] = pd.cut(data[column], num_bins)

def preprocess_data(df):
    # Data Cleaning
    clean_data(df)
    
    # Data Transformation
    transform_data(df,"Fare")
    
    # Data Reduction
    data_Reduction(df)
    
    # Data Discretization
    data_discretization(df, {'Age': 5, 'Fare': 10})
    
    return df

if __name__ == "__main__":
    dataset_path = "dataset.csv"  # Assuming dataset path is known
    
    # Load dataset
    df = pd.read_csv(dataset_path)
    
    # Preprocess data
    df_processed = preprocess_data(df)
    
    # Save resulting dataframe to CSV
    df_processed.to_csv("res_dpre.csv", index=False)
