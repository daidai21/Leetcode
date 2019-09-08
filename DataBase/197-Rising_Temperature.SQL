-- TO_DAYS  
SELECT
    wt1.Id
FROM
    Weather wt1,
    Weather wt2
WHERE
    wt1.Temperature > wt2.Temperature
    AND TO_DAYS(wt1.RecordDate) - TO_DAYS(wt2.RecordDate) = 1;
