import pandas as pd

def create_driver_features(df):
    driver_features = df.groupby(['driverId', 'year']).agg({
        'points_driver': ['sum', 'mean', 'max'],
        'wins_driver': 'sum',
        'positionOrder': ['mean', 'min'],
        'laps': 'sum'
    }).reset_index()
    
    driver_features.columns = [
        'driverId', 'year', 
        'driver_total_points', 'driver_avg_points', 'driver_max_points',
        'driver_total_wins', 
        'driver_avg_finish', 'driver_best_finish',
        'driver_total_laps'
    ]
    
    return driver_features