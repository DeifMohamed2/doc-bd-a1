import pandas as pd
from sklearn.cluster import KMeans

def k_means_clustering(df, k):
    data_for_kmeans = df[['Parch', 'SibSp']]

#    Initialize the KMeans model with k=3
    kmeans = KMeans(n_clusters=k)

    # Fit the model to the data
    kmeans.fit(data_for_kmeans)


    cluster_counts = pd.Series(kmeans.labels_).value_counts()

    # Save the cluster counts to a text file
    with open('k.txt', 'w') as f:
      for cluster, count in cluster_counts.items():
        f.write(f'Cluster {cluster}: {count}\n')

if __name__ == "__main__":
    # Load dataset
    df = pd.read_csv("dataset.csv")

    # Apply K-means clustering
    k_means_clustering(df, k=3)
