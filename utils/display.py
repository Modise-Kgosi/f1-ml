import pandas as pd

def format_predictions(predictions_df, drivers_df, constructors_df):
    """Format predictions with readable names"""
    # Add driver names
    if 'driverId' in predictions_df.columns:
        driver_names = drivers_df.copy()
        driver_names['driver_name'] = driver_names['forename'] + ' ' + driver_names['surname']
        predictions_df = predictions_df.merge(
            driver_names[['driverId', 'driver_name']], 
            on='driverId'
        )
    
    # Add constructor names
    if 'constructorId' in predictions_df.columns:
        predictions_df = predictions_df.merge(
            constructors_df[['constructorId', 'name']], 
            on='constructorId'
        )
        predictions_df = predictions_df.rename(columns={'name': 'team'})
    
    # Format probabilities
    predictions_df['win_probability'] = (predictions_df['champion_prob']
        .apply(lambda x: f"{float(x.strip('%')):.1f}%"))
    
    # Arrange columns
    if 'driverId' in predictions_df.columns:
        display_df = predictions_df[['driver_name', 'team', 'win_probability']]
    else:
        display_df = predictions_df[['team', 'win_probability']]
        
    return display_df