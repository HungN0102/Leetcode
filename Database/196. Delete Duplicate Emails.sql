DELETE FROM person
WHERE id not in (SELECT ID FROM
(SELECT email,
       MIN(ID) as ID
    FROM person
    GROUP BY email) as temp)