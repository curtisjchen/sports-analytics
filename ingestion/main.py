from ingestion.sources.nba_games import fetch_games
from ingestion.loaders.postgres import load_games
def main():
    season = '2024-25'
    print(f"Fetching games for season {season}...")
    games_df = fetch_games(season)
    print(len(games_df))
    try:
        load_games(games_df)
        print("Games loaded successfully.")
    except Exception as e:
        print(f"Error occurred while loading games: {e}")

if __name__ == "__main__":
    main()
