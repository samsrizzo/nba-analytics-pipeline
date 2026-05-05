import pandas as pd

def transform_player_game_logs(df: pd.DataFrame) -> pd.DataFrame:
    
    df = df.copy()                                                  
    df.columns = df.columns.str.lower()
    cols_to_drop = ['season_id', 'video_available', 'nickname']
    df = df.drop(columns = cols_to_drop, errors="ignore")

    df['game_date'] = pd.to_datetime(df['game_date'])              

    pct_cols = ['fg_pct', 'fg3_pct', 'ft_pct']                      
    df[pct_cols] = df[pct_cols].fillna(0)

    df = df.drop_duplicates(subset=['player_id', 'game_id'])        

    return df

def transform_team_game_logs(df: pd.DataFrame) -> pd.DataFrame:
    
    df = df.copy()                                                  
    df.columns = df.columns.str.lower()
    cols_to_drop = ['season_id', 'video_available']
    df = df.drop(columns = cols_to_drop, errors="ignore")

    df['game_date'] = pd.to_datetime(df['game_date'])              

    pct_cols = ['fg_pct', 'fg3_pct', 'ft_pct']                      
    df[pct_cols] = df[pct_cols].fillna(0)

    df = df.drop_duplicates(subset=['team_id', 'game_id'])        

    return df

if __name__ == "__main__":
      from extract import fetch_player_game_logs, fetch_team_game_logs

      player_logs = fetch_player_game_logs()
      team_logs = fetch_team_game_logs()

      player_transformed = transform_player_game_logs(player_logs)
      team_transformed = transform_team_game_logs(team_logs)

      print(player_transformed.shape)
      print(player_transformed.dtypes)
      print(team_transformed.shape)
      print(team_transformed.dtypes)