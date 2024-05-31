# Write your MySQL query statement below
(select u.name results from users u,movies m,movierating r
where r.user_id = u.user_id and m.movie_id = r.movie_id
group by u.user_id  
order by count(*) desc,u.name limit 1)
union all
(select m.title results from movies m,movierating r
where r.movie_id = m.movie_id and Month(r.created_at) = 2 and year(r.created_at) = 2020
group by r.movie_id
order by avg(r.rating) desc,m.title limit 1
)