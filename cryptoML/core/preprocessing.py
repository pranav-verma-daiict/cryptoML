import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import json

def load_and_preprocess(log_file: str):
    df = pd.read_json(log_file, lines=True)
    
    # Simple feature engineering
    df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
    df['event_type_encoded'] = pd.Categorical(df['event_type']).codes
    df['log_level_encoded'] = pd.Categorical(df['log_level']).codes
    
    features = ['hour', 'event_type_encoded', 'log_level_encoded']
    X = df[features].fillna(0)
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    print(f"Preprocessed {len(X)} samples")
    return X_scaled, scaler