# preprocessing/data_merger.py
import pandas as pd

def merge_data(cleaned_data):
    try:
        races = cleaned_data['races']
        results = cleaned_data['results']
        driver_standings = cleaned_data['driver_standings']
        constructor_standings = cleaned_data['constructor_standings']
        drivers = cleaned_data['drivers']
        constructors = cleaned_data['constructors']
        
        # Merge datasets
        df = results.merge(races, on='raceId') \
                    .merge(driver_standings, on=['raceId', 'driverId'], suffixes=('', '_driver')) \
                    .merge(constructor_standings, on=['raceId', 'constructorId'], suffixes=('', '_constructor')) \
                    .merge(drivers, on='driverId') \
                    .merge(constructors, on='constructorId')
        
        # Sort by year and round
        df = df.sort_values(['year', 'round'])
        
        print(f"✅ Merged dataset shape: {df.shape}")
        return df
    except KeyError as e:
        print(f"❌ Missing dataset in merge: {str(e)}")
        return pd.DataFrame()
    except Exception as e:
        print(f"❌ Error during merge: {str(e)}")
        return pd.DataFrame()