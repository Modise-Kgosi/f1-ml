import pandas as pd

def create_constructor_features(df):
    # Calculate completion rate
    total_races = df.groupby(['constructorId', 'year']).size().reset_index(name='total_races')
    completed_races = df[df['statusId'] == 1].groupby(['constructorId', 'year']).size().reset_index(name='completed_races')
    completion_rate = pd.merge(total_races, completed_races, on=['constructorId', 'year'], how='left')
    completion_rate['constructor_completion_rate'] = (completion_rate['completed_races'] / completion_rate['total_races']).fillna(0)

    # Calculate other features
    constructor_features = df.groupby(['constructorId', 'year']).agg({
        'points_constructor': ['sum', 'mean', 'max'],
        'wins_constructor': 'sum',
        'positionOrder': ['mean', 'min'],
        'laps': 'sum'
    }).reset_index()

    # Flatten column names
    constructor_features.columns = [
        'constructorId', 'year',
        'constructor_total_points', 'constructor_avg_points', 'constructor_max_points',
        'constructor_total_wins',
        'constructor_avg_finish', 'constructor_best_finish',
        'constructor_total_laps'
    ]

    # Merge completion rate
    constructor_features = pd.merge(
        constructor_features,
        completion_rate[['constructorId', 'year', 'constructor_completion_rate']],
        on=['constructorId', 'year'],
        how='left'
    )

    return constructor_features