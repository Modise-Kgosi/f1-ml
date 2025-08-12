from sklearn.ensemble import RandomForestClassifier

def train_wdc_model(X_train, y_wdc_train):
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=5,
        random_state=42,
        class_weight='balanced'
    )
    model.fit(X_train, y_wdc_train)
    print("✅ WDC model trained")
    return model

def train_wcc_model(X_train, y_wcc_train):
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=5,
        random_state=42,
        class_weight='balanced'
    )
    model.fit(X_train, y_wcc_train)
    print("✅ WCC model trained")
    return model