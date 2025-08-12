from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

def train_wdc_model(X_train, y_wdc_train):
    """Train the WDC prediction model"""
    print("\nTraining WDC Model:")
    print(f"Total samples: {len(y_wdc_train)}")
    print(f"Champions: {sum(y_wdc_train)} ({sum(y_wdc_train)/len(y_wdc_train)*100:.1f}%)")
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_train)
    
    model = RandomForestClassifier(
        n_estimators=500,
        max_depth=8,
        min_samples_split=4,
        min_samples_leaf=2,
        class_weight='balanced',
        random_state=42
    )
    
    model.fit(X_scaled, y_wdc_train)
    model.scaler = scaler  # Attach scaler to model
    return model

def train_wcc_model(X_train, y_wcc_train):
    """Train the WCC prediction model"""
    print("\nTraining WCC Model:")
    print(f"Total samples: {len(y_wcc_train)}")
    print(f"Champions: {sum(y_wcc_train)} ({sum(y_wcc_train)/len(y_wcc_train)*100:.1f}%)")
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_train)
    
    model = RandomForestClassifier(
        n_estimators=500,
        max_depth=8,
        min_samples_split=4,
        min_samples_leaf=2,
        class_weight='balanced',
        random_state=42
    )
    
    model.fit(X_scaled, y_wcc_train)
    model.scaler = scaler  # Attach scaler to model
    return model