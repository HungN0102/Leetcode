# Write your MySQL query statement below
SELECT  d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary
    FROM Employee e
    INNER JOIN (SELECT e.departmentID,
                       MAX(e.salary) AS Salary
                    FROM Employee e
                    GROUP BY e.departmentID) as p
    ON e.departmentId = p.departmentId
    AND p.Salary = e.salary
    LEFT JOIN Department d
    ON e.departmentId = d.id