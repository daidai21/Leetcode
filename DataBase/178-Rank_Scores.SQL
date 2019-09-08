SELECT
    s1.score 'Score',
    COUNT( DISTINCT s2.score) 'Rank'
FROM
    Scores s1
    INNER JOIN Scores s2
    ON s1.score <= s2.score
GROUP BY
    s1.id,
    s1.score
ORDER BY
    s1.score DESC;


SELECT
    Score,
    (
        SELECT
            COUNT( DISTINCT Score )
        FROM
            Scores
        WHERE
            Score >= s.Score
    ) Rank
FROM
    Scores s
ORDER BY
    Score desc;

