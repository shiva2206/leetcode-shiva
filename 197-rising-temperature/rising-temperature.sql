# Write your MySQL query statement below
select w1.id Id  from weather w1
left join weather w2 on datediff(w2.recordDate,w1.recordDate) = -1
where  w1.temperature > w2.temperature