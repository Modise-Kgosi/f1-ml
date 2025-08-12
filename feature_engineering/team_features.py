def add_team_changes(features_df):
    """Track significant team changes"""
    # Add dictionary of team principal changes by year and team
    team_changes = {
        2024: [1, 2],  # Teams with principal changes
        2023: [3, 4],
        # ... add historical data
    }
    
    features_df['team_principal_change'] = features_df.apply(
        lambda x: x['constructorId'] in team_changes.get(x['year'], []),
        axis=1
    )
    return features_df