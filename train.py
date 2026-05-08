import joblib
import sys
from pathlib import Path

sys.path.append(r'C:\Users\srizz\coding\nba-analytics-pipeline\etl')
sys.path.append(r'C:\Users\srizz\coding\nba-analytics-pipeline\models')

from extract import fetch_player_game_logs, fetch_team_game_logs
from transform import transform_player_game_logs, transform_team_game_logs
from features import calculate_player_features, calculate_team_features
from player_performance import train_player_performance_model, FEATURES as PLAYER_FEATURES
from game_outcome import train_game_outcome_model, FEATURES as GAME_FEATURES

ARTIFACTS_DIR = Path(__file__).parent / 'artifacts'

def train_models():
    
    print("Featching Logs...")
    player_logs = fetch_player_game_logs()
    team_logs = fetch_team_game_logs()

    print("Transforming Logs...")
    player_logs = transform_player_game_logs(player_logs)
    team_logs = transform_team_game_logs(team_logs)

    print("Calculating Features...")
    player_logs = calculate_player_features(player_logs, team_logs)
    team_logs = calculate_team_features(team_logs)
    
    print("Training Models...")
    player_performance_model = train_player_performance_model(player_logs)
    game_outcome_model = train_game_outcome_model(team_logs)
    
    ARTIFACTS_DIR.mkdir(exist_ok=True)
    joblib.dump(player_performance_model, ARTIFACTS_DIR / 'player_performance_model.joblib')
    joblib.dump(PLAYER_FEATURES, ARTIFACTS_DIR / 'player_features.joblib')
    joblib.dump(game_outcome_model, ARTIFACTS_DIR / 'game_outcome_model.joblib')
    joblib.dump(GAME_FEATURES, ARTIFACTS_DIR / 'game_features.joblib') 
    print(f"Artifcats saved to {ARTIFACTS_DIR}")
    
if __name__ == "__main__":
    train_models()

