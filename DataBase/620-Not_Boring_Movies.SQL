-- ORDER BY * DESC  两个联合使用
SELECT
    id,
    movie,
    description,
    rating
FROM
    cinema
WHERE
    MOD(id, 2) = 1
    AND description != 'boring'
ORDER BY
    rating DESC;
