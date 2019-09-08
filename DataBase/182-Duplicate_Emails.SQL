-- GROUP BY  聚合函数来使用
-- COUNT()  返回匹配指定条件的行数
-- HAVING  筛选分组后的各组数据 GROUP BY
SELECT
    Email
FROM
    Person
GROUP BY
    Email
HAVING
    COUNT(Email) >= 2;


SELECT
    Email
FROM
    (
        SELECT
            Email,
            COUNT(Email) as num
        FROM
            Person
        GROUP BY
            Email
    ) AS statistic
WHERE
    num > 1;
