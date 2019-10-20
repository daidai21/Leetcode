-- Runtime: 197 ms, faster than 25.25% of MySQL online submissions for Human Traffic of Stadium.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Human Traffic of Stadium.
-- Write your MySQL query statement below
SELECT DISTINCT s1.*
FROM stadium s1, stadium s2, stadium s3
WHERE s1.people > 99 AND s2.people > 99 AND s3.people > 99 AND (
    (s1.id - s2.id = 1 AND s1.id - s3.id = 2 AND s2.id - s3.id = 1) OR -- s1 s2 s3
    (s2.id - s1.id = 1 AND s2.id - s3.id = 2 AND s1.id - s3.id = 1) OR -- s2 s1 s3
    (s3.id - s2.id = 1 AND s2.id - s1.id = 1 AND s3.id - s1.id = 2)    -- s3 s2 s1
)
ORDER BY s1.id;
