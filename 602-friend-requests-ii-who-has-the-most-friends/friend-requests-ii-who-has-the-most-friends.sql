# Write your MySQL query statement below




select fir.id id, sum(fir.num) num from 
(select requester_id id, count(*) num from requestAccepted group by requester_id 
union all
select accepter_id id,count(*) num from requestAccepted group by accepter_id ) fir
group by fir.id
order by num desc limit 1
