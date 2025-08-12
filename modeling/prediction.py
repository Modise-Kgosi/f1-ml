from config.paths import MODEL_FEATURES

def predict_current_season(model, features_df, year, target_type='wdc'):
    current_data = features_df[features_df['year'] == year - 1].copy()
    
    if current_data.empty:
        print(f"❌ No data available for prediction year {year}")
        return None
    
    X_current = current_data[MODEL_FEATURES]
    current_data['champion_prob'] = model.predict_proba(X_current)[:, 1]
    
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
    
    print(result)
    return result