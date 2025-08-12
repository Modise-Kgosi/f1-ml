import pandas as pd
import numpy as np

def create_constructor_features(df):
    """Create constructor-specific features"""
    # Calculate season-level stats
    constructor_features = df.groupby(['constructorId', 'year']).agg({
        'points_constructor': ['sum', 'mean', 'max'],
        'wins_constructor': 'sum',
        'positionOrder': ['mean', 'min', 'std'],
        'laps': ['sum', 'mean'],
        'statusId': lambda x: (x == 1).mean(),
        'grid': ['mean', 'min']
    }).reset_index()

    # Flatten column names
    constructor_features.columns = [
        'constructorId', 'year',
        'constructor_total_points', 'constructor_avg_points', 'constructor_max_points',
        'constructor_wins',
        'constructor_avg_position', 'constructor_best_position', 'constructor_position_std',
        'constructor_total_laps', 'constructor_avg_laps',
        'constructor_completion_rate',
        'constructor_avg_grid', 'constructor_best_grid'
    ]

    # Calculate recent form
    recent_stats = df.sort_values(['year', 'round']).groupby(
        ['constructorId', 'year']
    ).agg({
        'points_constructor': lambda x: x.tail(3).mean(),
        'positionOrder': lambda x: x.tail(3).mean()
    }).reset_index()

    # Rename recent stats columns
    recent_stats.columns = [
        'constructorId', 'year',
        'constructor_recent_points', 'constructor_recent_position'
    ]

    # Merge all features
    constructor_features = pd.merge(
        constructor_features,
        recent_stats,
        on=['constructorId', 'year'],
        how='left'
    )

    # Fill NaN values
    constructor_features = constructor_features.fillna({
        'constructor_recent_points': 0,
        'constructor_recent_position': constructor_features['constructor_avg_position']
    })

    return constructor_features