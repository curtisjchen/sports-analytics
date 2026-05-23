{{ config(materialized='table') }}

WITH game_ratings AS (
    select
        a.game_id,
        a.team_id,
        a.team_name,
        a.team_abbreviation,
        a.pts / NULLIF(a.possessions, 0) * 100 as offensive_rating,
        b.opponent_pts / NULLIF(a.possessions, 0) * 100 as defensive_rating
    from {{ ref('int_team_game_stats') }} as a
    left join (
        select 
            game_id, 
            team_id, 
            pts as opponent_pts
        from {{ ref('int_team_game_stats') }}
    ) as b
    on a.game_id = b.game_id and a.team_id != b.team_id
),

team_averages AS (
    select
        team_id,
        team_name,
        team_abbreviation,
        avg(offensive_rating) as offensive_rating,
        avg(defensive_rating) as defensive_rating,
        avg(offensive_rating) - avg(defensive_rating) as net_rating
    from game_ratings
    group by team_id, team_name, team_abbreviation
)

SELECT * FROM team_averages
ORDER BY net_rating DESC