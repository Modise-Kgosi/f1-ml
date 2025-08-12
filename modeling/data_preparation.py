from config.paths import MODEL_FEATURES

def prepare_model_data(features_df, test_year_start=2018):
    # Create a copy to avoid modifications to original
    features_df = features_df.copy()
    
    # Reset index to avoid duplicate indices
    features_df = features_df.reset_index(drop=True)
    
    # Prepare datasets
    X = features_df[MODEL_FEATURES]
    y_wdc = features_df['wdc_target']
    y_wcc = features_df['wcc_target']
    
    # Time-based split
    train_mask = features_df['year'] < test_year_start
    test_mask = features_df['year'] >= test_year_start
    
    X_train = X[train_mask]
    X_test = X[test_mask]
    y_wdc_train = y_wdc[train_mask]
    y_wdc_test = y_wdc[test_mask]
    y_wcc_train = y_wcc[train_mask]
    y_wcc_test = y_wcc[test_mask]
    
    print(f"✅ Training data: {X_train.shape}, Test data: {X_test.shape}")
    return X_train, X_test, y_wdc_train, y_wdc_test, y_wcc_train, y_wcc_test