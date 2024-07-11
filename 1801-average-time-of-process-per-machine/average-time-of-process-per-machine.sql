# Write your MySQL query statement below
select a1.machine_id, Round(avg(a2.timestamp - a1.timestamp),3) processing_time from Activity a1
inner join activity a2 on a1.machine_id = a2.machine_id and a1.process_id = a2.process_id
and a1.activity_type!= a2.activity_type
where a1.activity_type = 'start'

group by a1.machine_id
