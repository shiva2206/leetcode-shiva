# Write your MySQL query statement below
select user_id,concat(Upper(substring(name,1,1)),lower(substring(name,2))) name from users
order by user_id