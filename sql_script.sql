SELECT
    gender,
    COUNT(*) as count,
    CASE
        WHEN game = 'wwc' THEN 'WWC'
        WHEN game = 'hb' THEN 'HB'
        ELSE 'Unknown Game'
    END as game_name
FROM
    users
WHERE
    game IN ('wwc', 'hb')
GROUP BY
    gender, game;
