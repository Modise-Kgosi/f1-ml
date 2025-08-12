import pandas as pd
import numpy as np

def add_performance_features(df):
    """Add advanced performance metrics"""
    df = df.copy()
    
    # Qualifying performance
    df['qualifying_vs_finish'] = df['grid'] - df['positionOrder']
    df['qualifying_top_3'] = (df['grid'] <= 3).astype(int)
    
    # Points scoring consistency
    df['points_finishes'] = (df['points'] > 0).astype(int)
    
    # Relative performance
    df['position_vs_grid'] = df['positionOrder'] - df['grid']
    
    # Create season aggregates
    perf_features = df.groupby(['driverId', 'constructorId', 'year']).agg({
        'qualifying_vs_finish': ['mean', 'std'],
        'qualifying_top_3': 'sum',
        'points_finishes': 'sum',
        'position_vs_grid': ['mean', 'std']
    }).reset_index()
    
    # Flatten column names
    perf_features.columns = [
        'driverId', 'constructorId', 'year',
        'avg_qualifying_improvement', 'qualifying_consistency',
        'qualifying_top3_count', 'points_scoring_races',
        'avg_race_improvement', 'race_consistency'
    ]
    
    return perf_features