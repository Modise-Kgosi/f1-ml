from config.paths import MODEL_FEATURES
import numpy as np

def predict_current_season(model, features_df, year, target_type='wdc'):
    current_data = features_df[features_df['year'] == year - 1].copy()
    
    if current_data.empty:
        print(f"❌ No data available for prediction year {year}")
        return None
    
    X_current = current_data[MODEL_FEATURES]
    
    # Get probabilities and handle single class case
    proba = model.predict_proba(X_current)
    if proba.shape[1] == 1:
        # If only one class probability, assume it's for class 0
        champion_probs = 1 - proba[:, 0]
    else:
        # Normal case - use probability for class 1
        champion_probs = proba[:, 1]
    
    current_data['champion_prob'] = champion_probs
    
    if target_type == 'wdc':
        result = current_data[['driverId', 'constructorId', 'champion_prob']] \
            .sort_values('champion_prob', ascending=False) \
            .head(10)
        print(f"\n🏆 Top WDC Contenders for {year}:")
    else:
        result = current_data[['constructorId', 'champion_prob']] \
            .sort_values('champion_prob', ascending=False) \
            .head(5)
        print(f"\n🏆 Top WCC Contenders for {year}:")
    
    # Format probabilities as percentages
    result['champion_prob'] = result['champion_prob'].apply(lambda x: f"{x*100:.1f}%")
    print(result)
    return result