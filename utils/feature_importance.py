import matplotlib.pyplot as plt

def plot_feature_importance(model, feature_names, title):
    importances = model.feature_importances_
    sorted_idx = importances.argsort()[::-1]
    
    print(f"\n📊 {title} Feature Importance:")
    for i in sorted_idx:
        print(f"{feature_names[i]}: {importances[i]:.4f}")
    
    plt.figure(figsize=(10, 6))
    plt.barh(range(len(sorted_idx)), importances[sorted_idx], align='center')
    plt.yticks(range(len(sorted_idx)), [feature_names[i] for i in sorted_idx])
    plt.title(title)
    plt.xlabel("Feature Importance")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(f'{title.replace(" ", "_").lower()}_importance.png')
    plt.show()