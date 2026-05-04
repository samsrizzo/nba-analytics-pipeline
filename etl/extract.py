import time
import pandas as pd
from nba_api.stats.endpoints import leaguegamelog

SEASONS = ["2022-23", "2023-24", "2024-25"]

def fetch_player_game_logs():
    frames = []
    for season in SEASONS:
        gamelog = leaguegamelog.LeagueGameLog(
            season=season, 
            player_or_team_abbreviation = "P",
             season_type_all_star="Regular Season" ).get_data_frames()[0]
        gamelog['season'] = season
        frames.append(gamelog)
        time.sleep(1)
        pass
    return pd.concat(frames, ignore_index=True)

def fetch_team_game_logs():
    frames = []
    for season in SEASONS:
        gamelog = leaguegamelog.LeagueGameLog(
            season=season, 
            player_or_team_abbreviation = "T",
             season_type_all_star="Regular Season" ).get_data_frames()[0]
        gamelog['season'] = season
        frames.append(gamelog)
        time.sleep(1)
        pass
    return pd.concat(frames, ignore_index=True)

if __name__ == "__main__":  
        print("Fetching player game logs...")
        player_logs = fetch_player_game_logs()
        print(f"{len(player_logs):,} rows, {player_logs['PLAYER_ID'].nunique()} players")
        
        print("Fetching team game logs...")
        team_logs = fetch_team_game_logs()
        print(f"{len(team_logs):,} rows, {team_logs['TEAM_ID'].nunique()} teams")
        