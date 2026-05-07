import pandas as pd

def calculate_fantasy_points(player_performance_prediction):
    return (player_performance_prediction[:,0] + (1.25 * player_performance_prediction[:,1]) + 
            (1.5 * player_performance_prediction[:,2]) + (2 * player_performance_prediction[:,3]) + 
            (2 * player_performance_prediction[:,4]))

if __name__ == "__main__":
    import sys
    sys.path.append(r'C:\Users\srizz\coding\nba-analytics-pipeline\etl')
    from extract import fetch_player_game_logs, fetch_team_game_logs
    from transform import transform_player_game_logs, transform_team_game_logs
    from features import calculate_player_features
    from player_performance import train_player_performance_model, FEATURES

    player_logs = fetch_player_game_logs()
    team_logs = fetch_team_game_logs()

    player_logs = transform_player_game_logs(player_logs)
    team_logs = transform_team_game_logs(team_logs)

    player_logs = calculate_player_features(player_logs,team_logs)

    model = train_player_performance_model(player_logs)
    test = player_logs[player_logs['season']=="2024-25"]
    predictions = model.predict(test[FEATURES])

    fantasy_prediction = calculate_fantasy_points(predictions)
    print(f"Fantasy Predictions: {fantasy_prediction[:10]}")
    print(predictions[:10])