from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_model(model, X_test, y_test, model_name):
    # Get predictions
    y_pred = model.predict(X_test)
    
    # Get probabilities - handle the case where there's only one class
    y_prob = model.predict_proba(X_test)
    # If only one column, it means all predictions are for the negative class (0)
    if y_prob.shape[1] == 1:
        y_prob = 1 - y_prob  # Convert to probability of positive class
    else:
        y_prob = y_prob[:, 1]  # Probability of positive class
    
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
    total = len(y_test)
    positives = sum(y_test)
    print(f"\nClass Distribution in Test Set:")
    print(f"Total samples: {total}")
    print(f"Positive class (Champions): {positives} ({(positives/total)*100:.1f}%)")
    print(f"Negative class (Others): {total-positives} ({((total-positives)/total)*100:.1f}%)")
    
    return y_pred, y_prob