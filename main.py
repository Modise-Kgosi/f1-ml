# main.py
from data_loading.local_loader import load_datasets
from preprocessing.data_cleaner import (
    clean_races, clean_results, clean_driver_standings,
    clean_constructor_standings, clean_drivers, clean_constructors
)
from preprocessing.data_merger import merge_data
from feature_engineering.driver_features import create_driver_features
from feature_engineering.constructor_features import create_constructor_features
from feature_engineering.target_creation import create_targets
from modeling.data_preparation import prepare_model_data
from modeling.model_training import train_wdc_model, train_wcc_model
from modeling.evaluation import evaluate_model
from modeling.prediction import predict_current_season
from utils.feature_importance import plot_feature_importance
from config.paths import MODEL_FEATURES

def main():
    print("="*50)
    print("F1 CHAMPIONSHIP PREDICTION PIPELINE")
    print("="*50)
    
    # 1. Load data
    print("\n📂 LOADING DATA")
    datasets = load_datasets()
    
    # 2. Clean data
    print("\n🧹 CLEANING DATA")
    cleaned_data = {
        'races': clean_races(datasets['races']),
        'results': clean_results(datasets['results']),
        'driver_standings': clean_driver_standings(datasets['driver_standings']),
        'constructor_standings': clean_constructor_standings(datasets['constructor_standings']),
        'drivers': clean_drivers(datasets['drivers']),
        'constructors': clean_constructors(datasets['constructors'])
    }
    
    # 3. Merge data
    print("\n🔗 MERGING DATA")
    merged_df = merge_data(cleaned_data)
    
    # 4. Feature engineering
    print("\n🔧 CREATING FEATURES")
    driver_features = create_driver_features(merged_df)
    constructor_features = create_constructor_features(merged_df)
    
    # Combine features
    features_df = driver_features.merge(
        constructor_features, 
        on=['constructorId', 'year']
    )
    
    # Create targets
    features_df = create_targets(features_df, merged_df)
    
    # 5. Prepare modeling data
    print("\n⚙️ PREPARING MODEL DATA")
    (X_train, X_test, 
     y_wdc_train, y_wdc_test,
     y_wcc_train, y_wcc_test) = prepare_model_data(features_df)
    
    # 6. Train models
    print("\n🤖 TRAINING MODELS")
    wdc_model = train_wdc_model(X_train, y_wdc_train)
    wcc_model = train_wcc_model(X_train, y_wcc_train)
    
    # 7. Evaluate models
    print("\n📈 EVALUATING MODELS")
    wdc_pred, wdc_prob = evaluate_model(wdc_model, X_test, y_wdc_test, "WDC")
    wcc_pred, wcc_prob = evaluate_model(wcc_model, X_test, y_wcc_test, "WCC")
    
    # 8. Make predictions
    print("\n🔮 MAKING PREDICTIONS")
    predict_year = 2024
    predict_current_season(wdc_model, features_df, predict_year, 'wdc')
    predict_current_season(wcc_model, features_df, predict_year, 'wcc')
    
    # 9. Feature importance
    print("\n🔍 ANALYZING FEATURE IMPORTANCE")
    plot_feature_importance(wdc_model, MODEL_FEATURES, "WDC Prediction")
    plot_feature_importance(wcc_model, MODEL_FEATURES, "WCC Prediction")

if __name__ == "__main__":
    main()