select p.project_id,round(avg(e.experience_years),2) average_years from project p
inner join Employee e on e.employee_id = p.employee_id 
group by p.project_id