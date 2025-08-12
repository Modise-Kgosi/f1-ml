import pandas as pd
import numpy as np

def create_driver_features(df):
    """Create driver-specific features"""
    # Calculate season-level stats
    driver_features = df.groupby(['driverId', 'constructorId', 'year']).agg({
        'points_driver': ['sum', 'mean', 'max'],
        'wins_driver': 'sum',
        'positionOrder': ['mean', 'min', 'std'],
        'laps': ['sum', 'mean'],
        'statusId': lambda x: (x == 1).mean(),
        'grid': ['mean', 'min']
    }).reset_index()

    # Flatten column names
    driver_features.columns = [
        'driverId', 'constructorId', 'year',
        'driver_total_points', 'driver_avg_points', 'driver_max_points',
        'driver_wins',
        'driver_avg_position', 'driver_best_position', 'driver_position_std',
        'driver_total_laps', 'driver_avg_laps',
        'driver_completion_rate',
        'driver_avg_grid', 'driver_best_grid'
    ]

    # Calculate recent form (last 3 races)
    recent_stats = df.sort_values(['year', 'round']).groupby(
        ['driverId', 'constructorId', 'year']
    ).agg({
        'points_driver': lambda x: x.tail(3).mean(),
        'positionOrder': lambda x: x.tail(3).mean()
    }).reset_index()

    # Rename recent stats columns
    recent_stats.columns = [
        'driverId', 'constructorId', 'year',
        'driver_recent_points', 'driver_recent_position'
    ]

    # Merge all features
    driver_features = pd.merge(
        driver_features,
        recent_stats,
        on=['driverId', 'constructorId', 'year'],
        how='left'
    )

    # Fill NaN values
    driver_features = driver_features.fillna({
        'driver_recent_points': 0,
        'driver_recent_position': driver_features['driver_avg_position']
    })

    return driver_features