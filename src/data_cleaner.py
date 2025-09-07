import pandas as pd
import numpy as np

def clean_cyber_data(input_path, output_path):
    """
    Clean and preprocess the cybersecurity threat data
    """
    # Load the raw data
    df = pd.read_csv(input_path)
    
    print(f"Original data shape: {df.shape}")
    
    # Handle missing values
    df.fillna({
        "Financial Loss (in Million $)": 0,
        "Number of Affected Users": 0,
        "Defense Mechanism Used": "Unknown",
        "Incident Resolution Time (in Hours)": df['Incident Resolution Time (in Hours)'].median()
    }, inplace=True)
    
    # Convert data types
    df['Year'] = df['Year'].astype(int)
    df['Incident Resolution Time (in Hours)'] = df['Incident Resolution Time (in Hours)'].astype(float)
    
    # Create new features
    df['Loss per User'] = np.where(
        df['Number of Affected Users'] > 0,
        df['Financial Loss (in Million $)'] / df['Number of Affected Users'],
        0
    )
    
    # Bin resolution time
    df['Resolution Speed'] = pd.cut(
        df['Incident Resolution Time (in Hours)'],
        bins=[0, 24, 72, np.inf],
        labels=['Fast (<24h)', 'Medium (24-72h)', 'Slow (>72h)']
    )
    
    # Save cleaned data
    df.to_csv(output_path, index=False)
    print(f"Cleaned data shape: {df.shape}")
    print(f"Data saved to: {output_path}")
    
    return df

if __name__ == "__main__":
    # Clean the data
    input_path = "data/raw/cyber_threats.csv"
    output_path = "data/processed/cyber_threats_cleaned.csv"
    cleaned_df = clean_cyber_data(input_path, output_path)