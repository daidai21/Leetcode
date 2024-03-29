-- DELETE  删除表中的记录
DELETE p1
FROM
    Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id;


DELETE
FROM Person
WHERE Id not in (
    SELECT id
    FROM (
        SELECT min(Id) as id
        FROM Person
        GROUP BY Email
    ) t
)
;
