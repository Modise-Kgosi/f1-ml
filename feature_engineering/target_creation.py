import pandas as pd

def create_targets(features_df, df):
    # Add next year column
    features_df['next_year'] = features_df['year'] + 1
    
    # Get championship winners
    wdc_winners = df[df['position_driver'] == 1][['driverId', 'year']].drop_duplicates()
    wcc_winners = df[df['position_constructor'] == 1][['constructorId', 'year']].drop_duplicates()
    
    wdc_winners.columns = ['driverId', 'next_year']
    wcc_winners.columns = ['constructorId', 'next_year']
    
    # Merge targets
    features_df = features_df.merge(wdc_winners, on=['driverId', 'next_year'], how='left')
    features_df = features_df.merge(wcc_winners, on=['constructorId', 'next_year'], how='left')
    
    # Create binary targets
    features_df['wdc_target'] = features_df['year_y'].notna().astype(int)
    features_df['wcc_target'] = features_df['year'].notna().astype(int)
    
    # Clean up
    features_df = features_df.drop(columns=['year_x', 'year_y'])
    features_df = features_df.rename(columns={'next_year': 'year'})
    
    # Add completion rates
    total_laps_per_year = df.groupby('year')['laps'].sum().reset_index(name='total_laps_year')
    features_df = features_df.merge(total_laps_per_year, on='year', how='left')
    
    features_df['driver_completion_rate'] = features_df['driver_total_laps'] / features_df['total_laps_year']
    features_df['constructor_completion_rate'] = features_df['constructor_total_laps'] / features_df['total_laps_year']
    features_df = features_df.drop(columns=['total_laps_year'])
    
    # Fill NaNs
    features_df = features_df.fillna(0)
    
    print(f"✅ Feature dataset shape: {features_df.shape}")
    return features_df