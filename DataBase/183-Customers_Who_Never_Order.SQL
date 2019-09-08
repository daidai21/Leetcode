-- FROM后的表名起别名的时候可以省略AS
SELECT
    C.Name AS Customers
FROM
    Customers C
    LEFT JOIN Orders O
    ON C.Id = O.CustomerId
WHERE
    O.CustomerId IS NULL;


SELECT
    Name AS Customers
FROM
    Customers
WHERE
    Id NOT IN
    (
        SELECT
            CustomerId
        FROM
            Orders
    );
