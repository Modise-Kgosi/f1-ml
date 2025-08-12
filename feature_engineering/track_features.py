def add_track_features(features_df, races_df, circuits_df):
    """Add circuit-specific performance metrics"""
    weather_sensitive_tracks = [1, 2, 3, 4]  # Add actual track IDs
    
    circuit_stats = races_df.merge(circuits_df, on='circuitId')
    circuit_stats['is_weather_sensitive'] = circuit_stats['circuitId'].isin(weather_sensitive_tracks)
    
    return features_df.merge(
        circuit_stats[['year', 'is_weather_sensitive']],
        on='year',
        how='left'
    )