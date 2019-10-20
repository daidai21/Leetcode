-- Runtime: 699 ms, faster than 57.78% of MySQL online submissions for Department Top Three Salaries.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Department Top Three Salaries.
-- # Write your MySQL query statement below
SELECT d.Name AS "Department", e1.Name AS "Employee", e1.Salary
FROM Employee e1 JOIN Department d ON e1.DepartmentId = d.Id
WHERE 3 > (
    SELECT COUNT(DISTINCT e2.Salary)
    FROM Employee e2
    WHERE e2.Salary > e1.Salary AND e1.DepartmentId = e2.DepartmentId
);
