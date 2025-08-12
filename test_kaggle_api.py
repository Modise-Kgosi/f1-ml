import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd

def main():
    # Initialize API
    api = KaggleApi()
    api.authenticate()
    print("✅ Authentication successful")
    
    # Create download directory
    download_dir = './f1_data'
    os.makedirs(download_dir, exist_ok=True)
    
    # Download entire dataset
    print("Downloading dataset...")
    api.dataset_download_files(
        dataset='jtrotman/formula-1-race-data', 
        path=download_dir,
        unzip=True  # Automatically unzip files
    )
    
    # List downloaded files
    files = os.listdir(download_dir)
    print("\n✅ Downloaded files:")
    for f in files:
        print(f"- {f}")
    
    # Load a sample file
    try:
        print("\nLoading races.csv...")
        races = pd.read_csv(f'{download_dir}/races.csv')
        print(f"Success! Loaded {len(races)} races")
        print(races[['year', 'name', 'circuitId']].head(3))
    except Exception as e:
        print(f"Error loading data: {str(e)}")

if __name__ == "__main__":
    main()