import pandas as pd

def add_historical_features(features_df):
    """Add features about past championships"""
    # Create a copy to avoid modifying original
    df = features_df.copy()
    
    # Select columns to carry forward
    historical_columns = [
        'driver_total_points', 'driver_wins', 'driver_completion_rate',
        'constructor_total_points', 'constructor_wins', 'constructor_completion_rate'
    ]
    
    # Verify columns exist
    missing_cols = [col for col in historical_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns for historical features: {missing_cols}")
    
    # Create previous year data
    prev_year = df[['driverId', 'constructorId', 'year'] + historical_columns].copy()
    prev_year['year'] = prev_year['year'] + 1
    
    # Rename columns to indicate they're from previous year
    rename_dict = {col: f'prev_{col}' for col in historical_columns}
    prev_year = prev_year.rename(columns=rename_dict)
    
    # Merge with original features
    result = df.merge(
        prev_year,
        on=['driverId', 'constructorId', 'year'],
        how='left'
    )
    
    # Fill NaN values with 0 for first year drivers/constructors
    for new_col in rename_dict.values():
        if new_col not in result.columns:
            print(f"Warning: Column {new_col} not found, creating it")
            result[new_col] = 0
        else:
            result[new_col] = result[new_col].fillna(0)
    
    print("✅ Added historical features")
    return result