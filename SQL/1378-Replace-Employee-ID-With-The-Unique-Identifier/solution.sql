SELECT em.unique_id,e.name
FROM Employees e
LEFT JOIN EmployeeUNI em
    ON  em.id =e.id 
