# test_imports.py
from config.paths import DATASET_FILES, MODEL_FEATURES
from data_loading.local_loader import load_datasets

print("DATASET_FILES:", DATASET_FILES)
print("MODEL_FEATURES:", MODEL_FEATURES)
print("\nTesting data loader...")
datasets = load_datasets()
print("\nLoaded datasets:", list(datasets.keys()))