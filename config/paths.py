import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
#Dataset files mapping
DATASET_FILES = {
    'races': 'races.csv',
    'results': 'results.csv',
    'drivers': 'drivers.csv',
    'constructors': 'constructors.csv',
    'driver_standings': 'driver_standings.csv',
    'constructor_standings': 'constructor_standings.csv'
}
#feature list for modeling
MODEL_FEATURES = [
    # Current season features
    'driver_total_points', 'driver_avg_points', 'driver_max_points',
    'driver_wins', 'driver_avg_position', 'driver_best_position',
    'driver_position_std', 'driver_total_laps', 'driver_avg_laps',
    'driver_completion_rate', 'driver_avg_grid', 'driver_best_grid',
    'driver_recent_points', 'driver_recent_position',
    
    # Historical features
    'prev_driver_total_points', 'prev_driver_wins', 'prev_driver_completion_rate',
    
    # Constructor features
    'constructor_total_points', 'constructor_avg_points', 'constructor_max_points',
    'constructor_wins', 'constructor_avg_position', 'constructor_best_position',
    'constructor_position_std', 'constructor_total_laps', 'constructor_avg_laps',
    'constructor_completion_rate', 'constructor_avg_grid', 'constructor_best_grid',
    'constructor_recent_points', 'constructor_recent_position',
    
    # Historical constructor features
    'prev_constructor_total_points', 'prev_constructor_wins', 'prev_constructor_completion_rate'
]

def get_data_path(filename):
    return os.path.join(DATA_DIR, filename)

