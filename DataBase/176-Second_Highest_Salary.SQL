-- SELECT DISTINCT  返回唯一不同的值
-- ORDER BY × DESC  排序时按降序排序
-- LIMIT  前n行数据
-- OFFSET  跳过n行数据
SELECT
    ( SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET 1) SecondHighestSalary;
