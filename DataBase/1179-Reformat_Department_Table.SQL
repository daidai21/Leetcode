-- Runtime: 336 ms, faster than 31.54% of MySQL online submissions for Reformat Department Table.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Reformat Department Table.
SELECT
    id,
    SUM(CASE WHEN month = 'jan' THEN revenue ELSE null END) AS Jan_Revenue,
    SUM(CASE WHEN month = 'feb' THEN revenue ELSE null END) AS Feb_Revenue,
    SUM(CASE WHEN month = 'mar' THEN revenue ELSE null END) AS Mar_Revenue,
    SUM(CASE WHEN month = 'apr' THEN revenue ELSE null END) AS Apr_Revenue,
    SUM(CASE WHEN month = 'may' THEN revenue ELSE null END) AS May_Revenue,
    SUM(CASE WHEN month = 'jun' THEN revenue ELSE null END) AS Jun_Revenue,
    SUM(CASE WHEN month = 'jul' THEN revenue ELSE null END) AS Jul_Revenue,
    SUM(CASE WHEN month = 'aug' THEN revenue ELSE null END) AS Aug_Revenue,
    SUM(CASE WHEN month = 'sep' THEN revenue ELSE null END) AS Sep_Revenue,
    SUM(CASE WHEN month = 'oct' THEN revenue ELSE null END) AS Oct_Revenue,
    SUM(CASE WHEN month = 'nov' THEN revenue ELSE null END) AS Nov_Revenue,
    SUM(CASE WHEN month = 'dec' THEN revenue ELSE null END) AS Dec_Revenue
FROM
    department
GROUP BY
    id
ORDER BY id;
