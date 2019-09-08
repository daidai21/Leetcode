-- UPDATE  更新表中的记录
-- SET  与UPDATE一起用
-- CASE  函数
UPDATE
    salary
SET
    sex = CASE sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END;
