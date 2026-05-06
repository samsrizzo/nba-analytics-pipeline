import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score

FEATURES = ['pts_roll5', 'reb_roll5', 'ast_roll5', 'pts_roll10', 'reb_roll10', 'ast_roll10', 'is_home', 'days_rest', 'is_back_to_back']
TARGETS = ['wl']

def train_game_outcome_model(df) :
    df['wl'] = (df['wl'] == 'W').astype(int)

    train = df[df['season'] != '2024-25']
    test = df[df['season'] == '2024-25']

    X_train = train[FEATURES]
    X_test = test[FEATURES]
    y_train = train['wl']
    y_test = test['wl']

    model = GradientBoostingClassifier().fit(X_train,y_train)

    y_pred = model.predict(X_test)

    auc = roc_auc_score(y_test, y_pred)
    print(f"ROC-AUC: {auc:.4f}")

    return model

if __name__ == '__main__':
    import sys
    sys.path.append(r'C:\Users\srizz\coding\nba-analytics-pipeline\etl')
    from extract import fetch_team_game_logs
    from transform import transform_team_game_logs
    from features import  calculate_team_features

    team_logs = fetch_team_game_logs()
    team_logs = transform_team_game_logs(team_logs)
    team_logs = calculate_team_features(team_logs)

    train_game_outcome_model(team_logs)