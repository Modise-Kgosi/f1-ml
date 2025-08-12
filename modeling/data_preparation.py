from config.paths import MODEL_FEATURES

def prepare_model_data(features_df, test_year_start=2018):
    # Prepare datasets
    X = features_df[MODEL_FEATURES]
    y_wdc = features_df['wdc_target']
    y_wcc = features_df['wcc_target']
    
    # Time-based split
    train_idx = features_df[features_df['year'] < test_year_start].index
    test_idx = features_df[features_df['year'] >= test_year_start].index
    
    X_train = X.loc[train_idx]
    X_test = X.loc[test_idx]
    
    y_wdc_train = y_wdc.loc[train_idx]
    y_wdc_test = y_wdc.loc[test_idx]
    
    y_wcc_train = y_wcc.loc[train_idx]
    y_wcc_test = y_wcc.loc[test_idx]
    
    print(f"✅ Training data: {X_train.shape}, Test data: {X_test.shape}")
    
    return X_train, X_test, y_wdc_train, y_wdc_test, y_wcc_train, y_wcc_test