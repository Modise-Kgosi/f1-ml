import pandas as pd

def clean_races(races_df):
    return races_df[['raceId', 'year', 'round', 'circuitId']]

def clean_results(results_df):
    return results_df[['resultId', 'raceId', 'driverId', 'constructorId', 
                      'positionOrder', 'points', 'laps', 'statusId']]

def clean_driver_standings(driver_standings_df):
    cleaned = driver_standings_df[['driverStandingsId', 'raceId', 'driverId', 'points', 'position', 'wins']]
    cleaned = cleaned.rename(columns={
        'points': 'points_driver',
        'position': 'position_driver',
        'wins': 'wins_driver'  # Add this rename
    })
    return cleaned

def clean_constructor_standings(constructor_standings_df):
    cleaned = constructor_standings_df[['constructorStandingsId', 'raceId', 'constructorId', 'points', 'position', 'wins']]
    cleaned = cleaned.rename(columns={
        'points': 'points_constructor',
        'position': 'position_constructor',
        'wins': 'wins_constructor'  # Add this rename
    })
    return cleaned

def clean_drivers(drivers_df):
    return drivers_df[['driverId', 'driverRef']]

def clean_constructors(constructors_df):
    return constructors_df[['constructorId', 'constructorRef']]