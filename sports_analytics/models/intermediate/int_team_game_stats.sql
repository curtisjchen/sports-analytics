{{ config(materialized='view') }}
SELECT
    fga - oreb + tov + (0.44 * fta) AS possessions,
    ROUND(pts / NULLIF(2 * (fga + 0.44 * fta), 0), 3) as true_shooting_percentage,
    game_id, team_id, team_name, team_abbreviation, game_date, matchup, wl, pts, plus_minus
from {{ ref('stg_games') }}