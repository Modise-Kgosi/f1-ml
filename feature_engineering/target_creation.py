import pandas as pd

def create_targets(features_df, df):
    """Create target variables for WDC and WCC predictions"""
    features_df = features_df.copy()
    
    # Get WDC champions - using driver standings
    wdc_winners = df.sort_values(['year', 'round']).groupby('year').last()
    wdc_winners = df[
        (df['points_driver'] == df.groupby('year')['points_driver'].transform('max')) &
        (df['round'] == df.groupby('year')['round'].transform('max'))
    ][['driverId', 'year']].drop_duplicates()
    
    # Get WCC champions - using constructor standings
    wcc_winners = df[
        (df['points_constructor'] == df.groupby('year')['points_constructor'].transform('max')) &
        (df['round'] == df.groupby('year')['round'].transform('max'))
    ][['constructorId', 'year']].drop_duplicates()
    
    # Add next year column for prediction
    features_df['next_year'] = features_df['year'] + 1
    
    # Print verification stats
    print("\nFound WDC champions by year:")
    wdc_stats = wdc_winners.groupby('year').size()
    print(wdc_stats.head())
    print(f"Total WDC champions found: {len(wdc_winners)}")
    
    print("\nFound WCC champions by year:")
    wcc_stats = wcc_winners.groupby('year').size()
    print(wcc_stats.head())
    print(f"Total WCC champions found: {len(wcc_winners)}")
    
    # Create targets
    features_df = features_df.merge(
        wdc_winners.rename(columns={'year': 'next_year'}),
        on=['driverId', 'next_year'],
        how='left',
        indicator='wdc_merge'
    )
    
    features_df = features_df.merge(
        wcc_winners.rename(columns={'year': 'next_year'}),
        on=['constructorId', 'next_year'],
        how='left',
        indicator='wcc_merge'
    )
    
    features_df['wdc_target'] = (features_df['wdc_merge'] == 'both').astype(int)
    features_df['wcc_target'] = (features_df['wcc_merge'] == 'both').astype(int)
    
    features_df = features_df.drop(['next_year', 'wdc_merge', 'wcc_merge'], axis=1)
    
    return features_df