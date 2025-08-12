from config.paths import MODEL_FEATURES
import numpy as np
from utils.display import format_predictions

def predict_current_season(model, features_df, year, target_type='wdc', drivers_df=None, constructors_df=None):
    """Make predictions for the current season"""
    current_data = features_df[features_df['year'] == year - 1].copy()
    
    if current_data.empty:
        print(f"❌ No data available for prediction year {year}")
        return None
    
    X_current = current_data[MODEL_FEATURES]
    X_scaled = model.scaler.transform(X_current)
    
    # Get probabilities
    proba = model.predict_proba(X_scaled)
    champion_probs = proba[:, 1] if proba.shape[1] > 1 else 1 - proba[:, 0]
    
    current_data['champion_prob'] = champion_probs * 100  # Convert to percentage
    
    if target_type == 'wdc':
        result = current_data[['driverId', 'constructorId', 'champion_prob']]
        result = result.sort_values('champion_prob', ascending=False).head(10)
    else:
        # Group by constructor and take max probability
        result = current_data.groupby('constructorId')['champion_prob'].max().reset_index()
        result = result.sort_values('champion_prob', ascending=False).head(5)
    
    # Format results
    if drivers_df is not None and target_type == 'wdc':
        result = result.merge(drivers_df[['driverId', 'driverRef']], on='driverId', how='left')
    
    if constructors_df is not None:
        result = result.merge(constructors_df[['constructorId', 'name']], on='constructorId', how='left')
    
    # Print formatted results
    if target_type == 'wdc':
        print(f"\n🏆 Top WDC Contenders for {year}:")
        print(result[['driverRef', 'name', 'champion_prob']].to_string(index=False))
    else:
        print(f"\n🏆 Top WCC Contenders for {year}:")
        print(result[['name', 'champion_prob']].to_string(index=False))
    
    return result