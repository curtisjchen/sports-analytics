import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd

def get_connection():
    load_dotenv()
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return connection

def load_games(games_df):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS games (
            season_id VARCHAR(10),
            team_id INT,
            team_abbreviation VARCHAR(10),
            team_name VARCHAR(50),
            game_id VARCHAR(20),
            game_date DATE,
            matchup VARCHAR(100),
            wl VARCHAR(1),
            min VARCHAR(10),
            pts INT,
            fgm INT,
            fga INT,
            fg_pct FLOAT,
            fg3m INT,
            fg3a INT,
            fg3_pct FLOAT,
            ftm INT,
            fta INT,
            ft_pct FLOAT,
            oreb INT,
            dreb INT,
            reb INT,
            ast INT,
            stl INT,
            blk INT,
            tov INT,
            pf INT, plus_minus INT, PRIMARY KEY (game_id, team_id)
        )
    """)
    
    for _, row in games_df.iterrows():
        cursor.execute("""
            INSERT INTO games (season_id, team_id, team_abbreviation, team_name, game_id, game_date, matchup, wl, min, pts, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct, ftm, fta, ft_pct, oreb, dreb, reb, ast, stl, blk, tov, pf, plus_minus)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (game_id, team_id) DO NOTHING
        """, (row['SEASON_ID'], row['TEAM_ID'], row['TEAM_ABBREVIATION'], row['TEAM_NAME'], row['GAME_ID'], row['GAME_DATE'], row['MATCHUP'], row['WL'], row['MIN'], row['PTS'], row['FGM'], row['FGA'], row['FG_PCT'], row['FG3M'], row['FG3A'], row['FG3_PCT'], row['FTM'], row['FTA'], row['FT_PCT'], row['OREB'], row['DREB'], row['REB'], row['AST'], row['STL'], row['BLK'], row['TOV'], row['PF'], row['PLUS_MINUS']))
    
    connection.commit()
    cursor.close()
    connection.close()

# ['SEASON_ID', 'Player_ID', 'Game_ID', 'GAME_DATE', 'MATCHUP', 'WL', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PLUS_MINUS', 'VIDEO_AVAILABLE']
def load_players(players_df):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            season_id VARCHAR(10),
            player_id INT,
            game_id VARCHAR(20),
            game_date DATE,
            matchup VARCHAR(100),
            wl VARCHAR(1),
            min VARCHAR(10),
            fgm INT,
            fga INT,
            fg_pct FLOAT,
            fg3m INT,
            fg3a INT,
            fg3_pct FLOAT,
            ftm INT,
            fta INT,
            ft_pct FLOAT,
            oreb INT,
            dreb INT,
            reb INT,
            ast INT,
            stl INT,
            blk INT,
            tov INT,
            pf INT, pts INT, plus_minus INT, PRIMARY KEY (game_id, player_id)
        )
    """)
    for _, row in players_df.iterrows():
        cursor.execute("""
            INSERT INTO players (season_id, player_id, game_id, game_date, matchup, wl, min, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct, ftm, fta, ft_pct, oreb, dreb, reb, ast, stl, blk, tov, pf, pts, plus_minus)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (game_id, player_id) DO NOTHING
        """, (row['SEASON_ID'], row['Player_ID'], row['Game_ID'], pd.to_datetime(row['GAME_DATE']).date(), row['MATCHUP'], row['WL'], row['MIN'], row['FGM'], row['FGA'], row['FG_PCT'], row['FG3M'], row['FG3A'], row['FG3_PCT'], row['FTM'], row['FTA'], row['FT_PCT'], row['OREB'], row['DREB'], row['REB'], row['AST'], row['STL'], row['BLK'], row['TOV'], row['PF'], row['PTS'], row['PLUS_MINUS']))

    connection.commit()
    cursor.close()
    connection.close()
