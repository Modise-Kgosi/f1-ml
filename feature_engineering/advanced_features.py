import pandas as pd
import numpy as np

def calculate_form_features(df):
    """Calculate recent form and momentum features"""
    def last_n_races_stats(group, n=3):
        """Calculate statistics for last N races"""
        if len(group) < n:
            return pd.Series({
                'recent_points': group['points'].mean(),
                'recent_positions': group['positionOrder'].mean(),
                'recent_finish_rate': (group['statusId'] == 1).mean(),
                'recent_top5': (group['positionOrder'] <= 5).mean()
            })
            
        last_n = group.tail(n)
        return pd.Series({
            'recent_points': last_n['points'].mean(),
            'recent_positions': last_n['positionOrder'].mean(),
            'recent_finish_rate': (last_n['statusId'] == 1).mean(),
            'recent_top5': (last_n['positionOrder'] <= 5).mean()
        })
    
    # Calculate driver form
    driver_stats = df.sort_values(['year', 'round'])
    driver_groups = driver_stats.groupby(['driverId', 'year'])
    driver_form = driver_groups.apply(last_n_races_stats, include_groups=False).reset_index()
    
    # Rename columns for drivers
    driver_cols = ['driverId', 'year', 'driver_recent_points', 'driver_recent_positions', 
                  'driver_recent_finish_rate', 'driver_recent_top5']
    driver_form.columns = driver_cols
    
    # Calculate constructor form
    constructor_stats = df.sort_values(['year', 'round'])
    constructor_groups = constructor_stats.groupby(['constructorId', 'year'])
    constructor_form = constructor_groups.apply(last_n_races_stats, include_groups=False).reset_index()
    
    # Rename columns for constructors
    constructor_cols = ['constructorId', 'year', 'constructor_recent_points', 'constructor_recent_positions',
                       'constructor_recent_finish_rate', 'constructor_recent_top5']
    constructor_form.columns = constructor_cols
    
    return driver_form, constructor_form

def add_advanced_features(features_df, merged_df):
    """Add advanced performance metrics"""
    # Calculate form features
    driver_form, constructor_form = calculate_form_features(merged_df)
    
    # Merge form features
    features_df = features_df.merge(
        driver_form,
        on=['driverId', 'year'],
        how='left'
    )
    
    features_df = features_df.merge(
        constructor_form,
        on=['constructorId', 'year'],
        how='left'
    )
    
    # Fill any missing values
    for col in features_df.columns:
        if col.startswith(('driver_recent', 'constructor_recent')):
            features_df[col] = features_df[col].fillna(0)
            
    print("✅ Added advanced features")
    return features_df