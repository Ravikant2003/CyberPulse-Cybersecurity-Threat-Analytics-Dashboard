import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

def train_clustering_model():
    """
    Train a K-Means clustering model to segment cyber incidents into threat profiles
    """
    # Create directories if they don't exist
    os.makedirs('./models', exist_ok=True)
    os.makedirs('./data/processed', exist_ok=True)
    
    # Load cleaned data
    df = pd.read_csv('./data/processed/cyber_threats_cleaned.csv')
    
    # Select features for clustering
    features = df[['Financial Loss (in Million $)', 'Number of Affected Users', 
                  'Incident Resolution Time (in Hours)']]
    
    # Handle missing values
    features = features.replace([np.inf, -np.inf], np.nan)
    features = features.fillna(features.median())
    
    # Scale the features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    
    # Find optimal number of clusters using silhouette score (without detailed output)
    silhouette_scores = []
    k_range = range(2, 8)
    
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(scaled_features)
        score = silhouette_score(scaled_features, kmeans.labels_)
        silhouette_scores.append(score)
    
    # Choose optimal k
    optimal_k = k_range[np.argmax(silhouette_scores)]
    print(f"Created {optimal_k} distinct threat profiles based on data patterns")
    
    # Train final model with optimal k
    kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(scaled_features)
    
    # Analyze clusters
    cluster_summary = df.groupby('Cluster').agg({
        'Financial Loss (in Million $)': 'mean',
        'Number of Affected Users': 'mean',
        'Incident Resolution Time (in Hours)': 'mean'
    }).round(2)
    
    # Assign meaningful cluster names based on characteristics
    cluster_names = {}
    for cluster_id in range(optimal_k):
        cluster_data = cluster_summary.loc[cluster_id]
        
        financial_high = cluster_data['Financial Loss (in Million $)'] > cluster_summary['Financial Loss (in Million $)'].mean()
        users_high = cluster_data['Number of Affected Users'] > cluster_summary['Number of Affected Users'].mean()
        
        if financial_high and users_high:
            name = 'Critical: High Impact on Both'
        elif financial_high and not users_high:
            name = 'Targeted: High Financial Impact'
        elif not financial_high and users_high:
            name = 'Widespread: High User Impact'
        else:
            name = 'Standard: Moderate Impact'
            
        cluster_names[cluster_id] = name
    
    df['Threat Profile'] = df['Cluster'].map(cluster_names)
    
    # Save the model and scaler
    joblib.dump(kmeans, './models/kmeans_model.joblib')
    joblib.dump(scaler, './models/scaler.joblib')
    
    # Save data with clusters
    df.to_csv('./data/processed/cyber_threats_clustered.csv', index=False)
    
    print("Clustering complete! Threat profiles saved for dashboard visualization.")
    print(f"Generated {optimal_k} distinct threat categories for cybersecurity analysis.")
    
    return df, kmeans, scaler

if __name__ == "__main__":
    train_clustering_model()