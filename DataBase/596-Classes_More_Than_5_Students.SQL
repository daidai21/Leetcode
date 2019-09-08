-- COUNT(DISTINCT *)  表中 列中不重复的记录条数
SELECT
    class
FROM
    courses
GROUP BY
    class
HAVING
    COUNT(DISTINCT student) >= 5;
