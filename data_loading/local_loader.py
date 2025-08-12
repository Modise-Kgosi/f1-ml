# data_loading/local_loader.py
import pandas as pd
from config.paths import get_data_path, DATASET_FILES  # Added DATASET_FILES import

def load_datasets():
    datasets = {}
    for name, file in DATASET_FILES.items():
        try:
            file_path = get_data_path(file)
            datasets[name] = pd.read_csv(file_path)
            print(f"✅ Loaded {name}: {datasets[name].shape}")
        except FileNotFoundError:
            print(f"❌ File not found: {file_path}")
            datasets[name] = None
        except Exception as e:
            print(f"❌ Error loading {name}: {str(e)}")
            datasets[name] = None
    return datasets