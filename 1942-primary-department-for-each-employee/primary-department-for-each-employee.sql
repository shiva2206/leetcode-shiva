# Write your MySQL query statement below

select employee_id,department_id from Employee e1
group by employee_id
having count(*) =1  
union
select employee_id,department_id from Employee e1
where primary_flag = 'Y'
group by employee_id,department_id 
