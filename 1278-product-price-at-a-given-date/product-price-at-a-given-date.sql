# Write your MySQL query statement below
select distinct product_id ,10 as price from Products 
group by product_id
having min(change_date) > '2019-08-16'
union 
select distinct product_id ,new_price as price from products p
where (product_id,change_date) in (select product_id,max(change_date) change_date from Products where change_date <= '2019-08-16' group by product_id)