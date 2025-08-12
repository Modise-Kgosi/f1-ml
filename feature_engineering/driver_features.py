import pandas as pd

def create_driver_features(df):
    # Calculate completion rate
    total_races = df.groupby(['driverId', 'constructorId', 'year']).size().reset_index(name='total_races')
    completed_races = df[df['statusId'] == 1].groupby(['driverId', 'constructorId', 'year']).size().reset_index(name='completed_races')
    completion_rate = pd.merge(total_races, completed_races, on=['driverId', 'constructorId', 'year'], how='left')
    completion_rate['driver_completion_rate'] = (completion_rate['completed_races'] / completion_rate['total_races']).fillna(0)

    # Calculate other features
    driver_features = df.groupby(['driverId', 'constructorId', 'year']).agg({
        'points_driver': ['sum', 'mean', 'max'],
        'wins_driver': 'sum',
        'positionOrder': ['mean', 'min'],
        'laps': 'sum'
    }).reset_index()

    # Flatten column names
    driver_features.columns = [
        'driverId', 'constructorId', 'year',
        'driver_total_points', 'driver_avg_points', 'driver_max_points',
        'driver_total_wins',
        'driver_avg_finish', 'driver_best_finish',
        'driver_total_laps'
    ]

    # Merge completion rate
    driver_features = pd.merge(
        driver_features,
        completion_rate[['driverId', 'constructorId', 'year', 'driver_completion_rate']],
        on=['driverId', 'constructorId', 'year'],
        how='left'
    )

    return driver_features