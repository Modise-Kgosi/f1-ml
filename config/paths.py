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
    'driver_total_points', 'driver_avg_points', 'driver_max_points',
    'driver_total_wins', 'driver_avg_finish', 'driver_best_finish',
    'constructor_total_points', 'constructor_avg_points', 'constructor_max_points',
    'constructor_total_wins', 'constructor_avg_finish', 'constructor_best_finish',
    'driver_completion_rate', 'constructor_completion_rate'
]

def get_data_path(filename):
    return os.path.join(DATA_DIR, filename)

