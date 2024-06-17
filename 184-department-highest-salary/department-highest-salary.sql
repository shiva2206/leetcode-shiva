select d.name as Department ,e.name Employee ,  salary from Employee e
left join Department d on e.departmentId = d.id 
where (salary,e.departmentId) in 
(select max(e.salary) salary,departmentId from Employee e 
left join Department d on d.id = e.departmentId 
group by departmentId);