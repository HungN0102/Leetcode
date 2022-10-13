# Write your MySQL query statement below
SELECT IFNULL(
            (SELECT DISTINCT 
                    SALARY 
                FROM Employee
                WHERE SALARY IS NOT NULL
                ORDER BY SALARY DESC
                LiMIT 1
                OFFSET 1)
            , null) 
    AS SecondHighestSalary