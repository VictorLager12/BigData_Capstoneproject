import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_prepare_data(filepath):
    """
    Loads the hospital dataset and prepares it for clustering.

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        pandas.DataFrame: The DataFrame with relevant columns for clustering.
        pandas.DataFrame: The original DataFrame.
    """
    df = pd.read_csv(filepath)
    # For clustering, we'll use the latitude and longitude
    X = df[['Lat', 'Long']]
    return X, df

def find_optimal_clusters(data, max_k=10):
    """
    Determines the optimal number of clusters using the elbow method.

    Args:
        data (pandas.DataFrame): The data to cluster.
        max_k (int): The maximum number of clusters to test.
    """
    iters = range(2, max_k+1)
    sse = []
    for k in iters:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(data)
        sse.append(kmeans.inertia_)

    # Plotting the elbow curve
    plt.figure(figsize=(10, 6))
    plt.plot(iters, sse, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia')
    plt.title('Elbow Method for Optimal k')
    plt.grid(True)
    plt.savefig('elbow_plot.png')
    plt.close()


def train_and_evaluate_model(data, n_clusters):
    """
    Trains a K-Means clustering model and evaluates it.

    Args:
        data (pandas.DataFrame): The data to cluster.
        n_clusters (int): The number of clusters to form.

    Returns:
        sklearn.cluster.KMeans: The trained K-Means model.
        float: The silhouette score of the model.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(data)
    
    # Evaluate the model using silhouette score
    score = silhouette_score(data, kmeans.labels_)
    print(f"Silhouette Score for {n_clusters} clusters: {score}")
    
    return kmeans, score

def visualize_clusters(df_original, kmeans_model):
    """
    Visualizes the clusters on a scatter plot. This is an innovative way
    to make the clustering results more interpretable.

    Args:
        df_original (pandas.DataFrame): The original DataFrame with all columns.
        kmeans_model (sklearn.cluster.KMeans): The trained K-Means model.
    """
    df_clustered = df_original.copy()
    df_clustered['Cluster'] = kmeans_model.labels_

    plt.figure(figsize=(12, 8))
    sns.scatterplot(x='Long', y='Lat', hue='Cluster', data=df_clustered, palette='viridis', s=10, alpha=0.7)
    
    # Plotting the centroids
    centroids = kmeans_model.cluster_centers_
    plt.scatter(centroids[:, 1], centroids[:, 0], s=200, c='red', marker='X', label='Centroids')
    
    plt.title('Geographical Clustering of Health Facilities in Africa')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend(title='Cluster')
    plt.grid(True)
    plt.savefig('clusters_map.png')
    plt.close()
    
    # Save the clustered data to a CSV file for further analysis
    df_clustered.to_csv('cfa_clustered.csv', index=False)


# --- Main Execution ---
# 1. Load and Prepare Data
X, df_original = load_and_prepare_data('cfa_fully_cleaned.csv')

# 2. Find Optimal Number of Clusters
# Let's find the optimal k up to 10 clusters and generate the elbow plot
find_optimal_clusters(X, max_k=10)

# 3. Train, Evaluate, and Visualize
# Based on the elbow plot (and for the sake of clear visualization), let's choose k=5. 
# You can adjust this based on the generated elbow_plot.png
n_clusters = 5
kmeans_model, silhouette = train_and_evaluate_model(X, n_clusters=n_clusters)

# 4. (Innovation) Visualize the clusters
visualize_clusters(df_original, kmeans_model)