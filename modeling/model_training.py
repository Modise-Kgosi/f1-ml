from sklearn.ensemble import RandomForestClassifier

def train_wdc_model(X_train, y_wdc_train):
    # Check class distribution
    n_samples = len(y_wdc_train)
    n_positive = sum(y_wdc_train)
    
    print(f"Class distribution in training data:")
    print(f"Total samples: {n_samples}")
    print(f"Champions: {n_positive} ({n_positive/n_samples*100:.1f}%)")
    print(f"Non-champions: {n_samples-n_positive} ({(n_samples-n_positive)/n_samples*100:.1f}%)")
    
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42,
        class_weight='balanced',  # Handle class imbalance
        min_samples_leaf=5
    )
    model.fit(X_train, y_wdc_train)
    print("✅ WDC model trained")
    return model

def train_wcc_model(X_train, y_wcc_train):
    # Check class distribution
    n_samples = len(y_wcc_train)
    n_positive = sum(y_wcc_train)
    
    print(f"Class distribution in training data:")
    print(f"Total samples: {n_samples}")
    print(f"Champions: {n_positive} ({n_positive/n_samples*100:.1f}%)")
    print(f"Non-champions: {n_samples-n_positive} ({(n_samples-n_positive)/n_samples*100:.1f}%)")
    
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42,
        class_weight='balanced',  # Handle class imbalance
        min_samples_leaf=5
    )
    model.fit(X_train, y_wcc_train)
    print("✅ WCC model trained")
    return model