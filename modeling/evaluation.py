from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_model(model, X_test, y_test, model_name):
    """Evaluate model performance"""
    # Scale the test data using the model's scaler
    X_scaled = model.scaler.transform(X_test)
    
    # Get predictions
    y_pred = model.predict(X_scaled)
    y_prob = model.predict_proba(X_scaled)
    
    # Get probability for positive class
    if y_prob.shape[1] == 1:
        y_prob = 1 - y_prob[:, 0]
    else:
        y_prob = y_prob[:, 1]
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    
    # Print results
    print(f"\n{model_name} Model Performance:")
    print(f"Accuracy:  {accuracy:.3f}")
    print(f"Precision: {precision:.3f}")
    print(f"Recall:    {recall:.3f}")
    print(f"F1 Score:  {f1:.3f}")
    
    # Print class distribution
    print(f"\nClass Distribution in Test Set:")
    print(f"Total samples: {len(y_test)}")
    print(f"Positive class (Champions): {sum(y_test)} ({sum(y_test)/len(y_test)*100:.1f}%)")
    print(f"Negative class (Others): {len(y_test)-sum(y_test)} ({(1-sum(y_test)/len(y_test))*100:.1f}%)")
    
    return y_pred, y_prob