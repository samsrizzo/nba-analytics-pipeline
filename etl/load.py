import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "nba.db"
ENGINE = create_engine(f"sqlite:///{DB_PATH}")

def load_player_game_log(df):
    df.to_sql('player_game_logs', con = ENGINE, if_exists = 'replace', index = False)

def load_team_game_log(df):
    df.to_sql('team_game_logs', con = ENGINE, if_exists = 'replace', index = False)    


if __name__ == "__main__":
    from extract import fetch_player_game_logs, fetch_team_game_logs
    from transform import transform_player_game_logs, transform_team_game_logs

    player_logs = fetch_player_game_logs()
    team_logs = fetch_team_game_logs()

    player_logs = transform_player_game_logs(player_logs)
    team_logs = transform_team_game_logs(team_logs)

    load_player_game_log(player_logs)
    load_team_game_log(team_logs)