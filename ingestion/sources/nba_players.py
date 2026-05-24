import pandas as pd
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
import time

def get_nba_players_gamelog():
    players_list = [p for p in players.get_players() if p['is_active']]
    df_list = []

    for i, player in enumerate(players_list):
        player_id = player['id']
        if i % 10 == 0:
            print(f"Fetching {player['full_name']}... ({i+1}/{len(players_list)})")
        gamelog = playergamelog.PlayerGameLog(player_id=player_id, season='2024-25')
        df = gamelog.get_data_frames()[0]
        if not df.empty:
            df_list.append(df)
        time.sleep(0.5)

    final_df = pd.concat(df_list, ignore_index=True)
    return final_df
    

