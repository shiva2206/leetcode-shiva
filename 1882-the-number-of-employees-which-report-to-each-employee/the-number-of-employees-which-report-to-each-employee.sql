# Write your MySQL query statement below

select e1.employee_id,e1.name,e2.reports_count,e2.average_age from employees e1,(select reports_to,count(*) reports_count,round(avg(age),0) average_age from employees e2 group by reports_to)  e2

where e1.employee_id =e2.reports_to
order by employee_id
