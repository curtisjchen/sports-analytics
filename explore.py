from nba_api.stats.endpoints import playergamelog

gamelog = playergamelog.PlayerGameLog(player_id=2544, season='2024-25')
df = gamelog.get_data_frames()[0]
print(df.columns.tolist())
print(df.head(3))