import pandas as pd

def calculate_features(player_logs: pd.DataFrame, team_logs: pd.DataFrame) -> pd.DataFrame:
    
    sorted_player_logs = player_logs.sort_values(by=['player_id', 'game_date']).reset_index(drop=True)

    sorted_player_logs['pts_roll5'] = sorted_player_logs.groupby('player_id')['pts'].transform(lambda x: x.rolling(5, min_periods=1).mean())
    sorted_player_logs['reb_roll5'] = sorted_player_logs.groupby('player_id')['reb'].transform(lambda x: x.rolling(5, min_periods=1).mean())
    sorted_player_logs['ast_roll5'] = sorted_player_logs.groupby('player_id')['ast'].transform(lambda x: x.rolling(5, min_periods=1).mean())
    sorted_player_logs['blk_roll5'] = sorted_player_logs.groupby('player_id')['blk'].transform(lambda x: x.rolling(5, min_periods=1).mean())
    sorted_player_logs['stl_roll5'] = sorted_player_logs.groupby('player_id')['stl'].transform(lambda x: x.rolling(5, min_periods=1).mean())

    sorted_player_logs['pts_roll10'] = sorted_player_logs.groupby('player_id')['pts'].transform(lambda x: x.rolling(10, min_periods=1).mean())
    sorted_player_logs['reb_roll10'] = sorted_player_logs.groupby('player_id')['reb'].transform(lambda x: x.rolling(10, min_periods=1).mean())
    sorted_player_logs['ast_roll10'] = sorted_player_logs.groupby('player_id')['ast'].transform(lambda x: x.rolling(10, min_periods=1).mean())
    sorted_player_logs['blk_roll10'] = sorted_player_logs.groupby('player_id')['blk'].transform(lambda x: x.rolling(10, min_periods=1).mean())
    sorted_player_logs['stl_roll10'] = sorted_player_logs.groupby('player_id')['stl'].transform(lambda x: x.rolling(10, min_periods=1).mean())

    sorted_player_logs['is_home'] = sorted_player_logs['matchup'].str.contains('vs.')

    sorted_player_logs['days_rest'] = sorted_player_logs.groupby('player_id')['game_date'].transform(lambda x: x.diff())
    sorted_player_logs['days_rest'] = sorted_player_logs['days_rest'].dt.days
    sorted_player_logs['days_rest'] = sorted_player_logs['days_rest'].fillna(0).astype(int)

    sorted_player_logs['is_back_to_back'] = (sorted_player_logs['days_rest'] == 1)

    return sorted_player_logs


if __name__ == '__main__' :
    from extract import fetch_player_game_logs, fetch_team_game_logs
    from transform import transform_player_game_logs, transform_team_game_logs

    player_logs = fetch_player_game_logs()
    player_logs = transform_player_game_logs(player_logs)
    team_logs = fetch_team_game_logs()
    team_logs = transform_team_game_logs(team_logs)
    
    player_logs = calculate_features(player_logs, team_logs)

    print("First 10 rows with new features:")
    print(player_logs.head(10))