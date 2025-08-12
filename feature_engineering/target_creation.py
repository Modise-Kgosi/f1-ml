import pandas as pd

def create_targets(features_df, df):
    # Add next year column
    features_df = features_df.copy()
    features_df['next_year'] = features_df['year'] + 1
    
    # Get championship winners
    wdc_winners = df[df['position_driver'] == 1][['driverId', 'year']].drop_duplicates()
    wcc_winners = df[df['position_constructor'] == 1][['constructorId', 'year']].drop_duplicates()
    
    # Rename columns before merge
    wdc_winners = wdc_winners.rename(columns={'year': 'champion_year'})
    wcc_winners = wcc_winners.rename(columns={'year': 'champion_year'})
    
    # Merge targets
    features_df = pd.merge(
        features_df,
        wdc_winners,
        left_on=['driverId', 'next_year'],
        right_on=['driverId', 'champion_year'],
        how='left'
    )
    
    features_df = pd.merge(
        features_df,
        wcc_winners,
        left_on=['constructorId', 'next_year'],
        right_on=['constructorId', 'champion_year'],
        how='left',
        suffixes=('_wdc', '_wcc')
    )
    
    # Create binary targets
    features_df['wdc_target'] = features_df['champion_year_wdc'].notna().astype(int)
    features_df['wcc_target'] = features_df['champion_year_wcc'].notna().astype(int)
    
    # Clean up
    features_df = features_df.drop(columns=['champion_year_wdc', 'champion_year_wcc', 'next_year'])
    
    print(f"✅ Created target variables: WDC and WCC champions")
    return features_df