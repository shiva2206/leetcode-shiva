# Write your MySQL query statement below
select s.product_id, s.year as first_year,quantity,price from Sales s
where (s.product_id,s.year) in (select s.product_id , min(s.year) as first_year from sales s
inner join Product p on p.product_id = s.product_id
group by product_id)