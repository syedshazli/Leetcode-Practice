
# Write your MySQL query statement below
SELECT unique_id, name
FROM Employees
LEFT JOIN EmployeeUni
ON Employees.id = EmployeeUNI.id;
