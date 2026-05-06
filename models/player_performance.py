import pandas as pd
import xgboost
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error

FEATURES = ['pts_roll5', 'reb_roll5', 'ast_roll5', 'stl_roll5', 'blk_roll5', 'pts_roll10', 'reb_roll10', 'ast_roll10', 'stl_roll10', 'blk_roll10', 'is_home', 'days_rest', 'is_back_to_back']
TARGETS = ['pts', 'reb', 'ast', 'stl', 'blk']

def train_player_performance_model(df) :
    train = df[df['season'] != '2024-25']
    test = df[df['season'] == '2024-25']

    X_train = train[FEATURES]
    X_test = test[FEATURES]
    y_train = train[TARGETS]
    y_test = test[TARGETS]

    model = MultiOutputRegressor(xgboost.XGBRegressor()).fit(X_train,y_train)
    
    y_pred = model.predict(X_test)

    for i, target in enumerate(TARGETS):
        mae = mean_absolute_error(y_test[target], y_pred[:, i])
        rmse = root_mean_squared_error(y_test[target], y_pred[:, i])
        print(f"{target} — MAE: {mae:.2f}, RMSE: {rmse:.2f}")
    
    return model

if __name__ == '__main__':
    import sys
    sys.path.append(r'C:\Users\srizz\coding\nba-analytics-pipeline\etl')
    from extract import fetch_player_game_logs, fetch_team_game_logs
    from transform import transform_player_game_logs, transform_team_game_logs
    from features import calculate_features

    player_logs = fetch_player_game_logs()
    team_logs = fetch_team_game_logs()

    player_logs = transform_player_game_logs(player_logs)
    team_logs = transform_team_game_logs(team_logs)

    player_logs = calculate_features(player_logs,team_logs)

    train_player_performance_model(player_logs)