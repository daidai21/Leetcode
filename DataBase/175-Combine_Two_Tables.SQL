-- left join  从左表返回所有的行，即使右表中没有匹配。如果右表中没有匹配，则结果为 NULL
SELECT
    FirstName,
    LastName,
    City,
    State
FROM
    Person
    LEFT JOIN Address
    ON Person.PersonId = Address.PersonId;
