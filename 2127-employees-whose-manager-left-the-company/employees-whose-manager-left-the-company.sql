# Write your MySQL query statement below
select employee_id from Employees e1

where manager_id is not null and manager_id not in (select employee_id from employees) and salary<30000
order by employee_id