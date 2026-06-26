import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os

def load_and_preprocess(log_file: str):
    """Optimized for Synthetic Cybersecurity Logs"""
    print(f"[{os.getenv('AGENCY_ID', 'unknown')}] Loading {log_file}...")
    
    if log_file.endswith('.csv'):
        df = pd.read_csv(log_file, nrows=20000)   # adjustable
    else:
        df = pd.read_json(log_file, lines=True)
    
    print(f"Columns: {list(df.columns)}")
    
    # Feature Engineering for your dataset
    df['timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
    df['hour'] = df['timestamp'].dt.hour.fillna(0)
    df['day_of_week'] = df['timestamp'].dt.dayofweek.fillna(0)
    
    # Encode useful categoricals
    df['request_type_encoded'] = pd.Categorical(df['Request_Type']).codes
    df['status_code_encoded'] = pd.Categorical(df['Status_Code']).codes
    df['anomaly_flag_encoded'] = pd.Categorical(df['Anomaly_Flag']).codes
    
    # Select final features (5 dimensions for current Autoencoder)
    feature_cols = ['hour', 'day_of_week', 'request_type_encoded', 
                   'status_code_encoded', 'anomaly_flag_encoded']
    
    X = df[feature_cols].fillna(0).values
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    print(f"✅ Preprocessed {len(X)} real samples | Features: {X.shape[1]}")
    return X_scaled, scaler, feature_cols
