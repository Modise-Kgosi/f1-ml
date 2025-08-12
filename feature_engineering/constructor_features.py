import pandas as pd

def create_constructor_features(df):
    constructor_features = df.groupby(['constructorId', 'year']).agg({
        'points_constructor': ['sum', 'mean', 'max'],
        'wins_constructor': 'sum',
        'positionOrder': ['mean', 'min'],
        'laps': 'sum'
    }).reset_index()
    
    constructor_features.columns = [
        'constructorId', 'year', 
        'constructor_total_points', 'constructor_avg_points', 'constructor_max_points',
        'constructor_total_wins', 
        'constructor_avg_finish', 'constructor_best_finish',
        'constructor_total_laps'
    ]
    
    return constructor_features