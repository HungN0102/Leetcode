# Write your MySQL query statement below
SELECT DISTINCT l1.num AS ConsecutiveNums
    FROM Logs l1
    INNER JOIN logs l2 
    ON l1.id = l2.id - 1
    AND l1.num = l2.num
    INNER JOIN logs l3
    ON l1.id = l3.id + 1
    AND l1.num = l3.num