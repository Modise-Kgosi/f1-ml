import pandas as pd
import numpy as np

def clean_races(races_df):
    """Clean and prepare race data"""
    cleaned = races_df[['raceId', 'year', 'round', 'circuitId']].copy()
    return cleaned

def convert_lap_time(time_str):
    """Convert lap time string to seconds"""
    if pd.isna(time_str):
        return np.nan
    try:
        # Handle different time formats
        if ':' in str(time_str):
            # Format: 'mm:ss.ms'
            parts = time_str.split(':')
            minutes = float(parts[0])
            seconds = float(parts[1])
            return minutes * 60 + seconds
        else:
            # Format: 'ss.ms'
            return float(time_str)
    except (ValueError, AttributeError, IndexError):
        return np.nan

def clean_results(results_df):
    """Clean and prepare results data"""
    cleaned = results_df.copy()
    
    # Select relevant columns
    cleaned = cleaned[[
        'resultId', 'raceId', 'driverId', 'constructorId',
        'grid', 'position', 'positionOrder', 'points',
        'laps', 'statusId', 'rank'
    ]]
    
    # Convert numeric columns
    numeric_cols = ['grid', 'position', 'positionOrder', 'points', 'laps']
    for col in numeric_cols:
        cleaned[col] = pd.to_numeric(cleaned[col], errors='coerce')
    
    # Fill missing values with appropriate defaults
    default_values = {
        'grid': -1,
        'position': -1,
        'positionOrder': -1,
        'points': 0,
        'laps': 0,
        'statusId': -1,
        'rank': -1
    }
    
    # Use infer_objects() to handle downcasting warning
    cleaned = cleaned.fillna(default_values).infer_objects()
    
    return cleaned

def clean_driver_standings(driver_standings_df):
    """Clean and prepare driver standings data"""
    cleaned = driver_standings_df[['driverStandingsId', 'raceId', 'driverId', 
                                 'points', 'position', 'wins']].copy()
    cleaned = cleaned.rename(columns={
        'points': 'points_driver',
        'position': 'position_driver',
        'wins': 'wins_driver'
    })
    return cleaned

def clean_constructor_standings(constructor_standings_df):
    """Clean and prepare constructor standings data"""
    cleaned = constructor_standings_df[['constructorStandingsId', 'raceId', 
                                      'constructorId', 'points', 'position', 'wins']].copy()
    cleaned = cleaned.rename(columns={
        'points': 'points_constructor',
        'position': 'position_constructor',
        'wins': 'wins_constructor'
    })
    return cleaned

def clean_drivers(drivers_df):
    """Clean and prepare driver data"""
    cleaned = drivers_df[[
        'driverId', 'driverRef', 'forename', 'surname', 'nationality'
    ]].copy()
    cleaned['fullname'] = cleaned['forename'] + ' ' + cleaned['surname']
    return cleaned

def clean_constructors(constructors_df):
    """Clean and prepare constructor data"""
    return constructors_df[['constructorId', 'constructorRef', 'name', 'nationality']].copy()