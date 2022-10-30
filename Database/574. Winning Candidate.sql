# Write your MySQL query statement below
SELECT name
    FROM candidate c
    INNER JOIN (SELECT candidateId
    FROM Vote v
    GROUP BY 1
    ORDER BY COUNT(*) DESC
    LIMIT 1) as p
    ON c.id = p.candidateId