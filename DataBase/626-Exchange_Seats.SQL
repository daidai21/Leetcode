-- IF(expr1, expr2, expr3)  IF表达式 如果 expr1 是TRUE, 则 IF()的返回值为expr2; 否则返回值则为 expr3
SELECT
    IF (
        id < (
            SELECT
                COUNT(*)
            FROM
                seat
        ),
        IF (
            MOD(id, 2) = 0,
            id - 1,
            id + 1
        ),
        IF (
            MOD(id, 2) = 0,
            id - 1,
            id
        )
    ) as id, student
FROM
    seat
ORDER BY
    id ASC;


SELECT
    s1.id - 1 AS id,
    s1.student
FROM
    seat s1
WHERE
    s1.id MOD 2 = 0 UNION
SELECT
    s2.id + 1 AS id,
    s2.student
FROM
    seat s2
WHERE
    s2.id MOD 2 = 1
    AND s2.id != ( SELECT MAX(s3.id) FROM seat s3 ) UNION
SELECT
    s4.id AS id,
    s4.student
FROM
    seat s4
WHERE
    s4.id MOD 2 = 1 AND s4.id = ( SELECT MAX(s5.id) FROM seat s5 )
ORDER BY
    id;
