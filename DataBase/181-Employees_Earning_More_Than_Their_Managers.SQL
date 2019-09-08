-- INNE JOIN * ON  关键字在表中存在至少一个匹配时返回行
-- AS  为表名称或列名称指定别名
SELECT
    E1.NAME AS Employee
FROM
    Employee E1
    INNER JOIN Employee E2
    ON E1.ManagerId = E2.Id
    AND E1.Salary > E2.Salary;
