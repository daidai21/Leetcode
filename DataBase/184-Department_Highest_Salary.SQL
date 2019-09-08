SELECT
    D.Name Department,
    E.Name Employee,
    E.Salary
FROM
    Employee E,
    Department D,
    (
        SELECT
            DepartmentId,
            MAX(Salary) Salary
        FROM
            Employee
        GROUP BY
            DepartmentId
    ) M
WHERE
    E.DepartmentId = D.Id
    AND E.DepartmentId = M.DepartmentId
    AND E.Salary = M.Salary;
