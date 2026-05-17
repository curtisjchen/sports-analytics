from nba_api.stats.endpoints import leaguegamefinder

def fetch_games(season):
    lgf = leaguegamefinder.LeagueGameFinder(season_nullable=season, season_type_nullable="Regular Season")
    dfs = lgf.get_data_frames()
    return dfs[0]
