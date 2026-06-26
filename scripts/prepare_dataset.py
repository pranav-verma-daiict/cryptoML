import pandas as pd
import os
import numpy as np

def prepare_and_split_dataset(input_csv: str, output_dir: str = "data/sample_logs"):
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Loading {input_csv}...")
    df = pd.read_csv(input_csv)
    print(f"Loaded {len(df)} rows with columns: {list(df.columns)}")
    
    # Basic cleaning
    df = df.dropna(subset=['timestamp']) if 'timestamp' in df else df
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)  # shuffle
    
    # Split roughly 50/50 for two agencies
    split_idx = len(df) // 2
    agency1_df = df.iloc[:split_idx]
    agency2_df = df.iloc[split_idx:]
    
    # Save as JSONL (compatible with current code)
    agency1_df.to_json(f"{output_dir}/agency1_logs.jsonl", orient='records', lines=True)
    agency2_df.to_json(f"{output_dir}/agency2_logs.jsonl", orient='records', lines=True)
    
    print(f"✅ Split complete:")
    print(f"   Agency1: {len(agency1_df)} logs")
    print(f"   Agency2: {len(agency2_df)} logs")
    
    return df.columns.tolist()

if __name__ == "__main__":
    csv_file = "data/sample_logs/advanced_cybersecurity_data.csv"   # ← Change to your actual filename
    prepare_and_split_dataset(csv_file)
