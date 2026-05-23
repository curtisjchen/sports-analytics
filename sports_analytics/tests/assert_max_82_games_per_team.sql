SELECT team_id, count(distinct game_id) as games_played
FROM {{ ref('stg_games') }}
GROUP BY team_id
HAVING count(distinct game_id) > 82