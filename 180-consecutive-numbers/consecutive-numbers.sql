# Write your MySQL query statement below
select distinct one.num ConsecutiveNums from logs one,logs two,logs three
where one.id+1 = two.id and two.id+1 = three.id and one.num = two.num and two.num = three.num