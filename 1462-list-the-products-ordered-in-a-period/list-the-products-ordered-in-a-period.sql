# Write your MySQL query statement below
select p.product_name, sum(o.unit) unit from products p
inner join Orders o on o.product_id = p.product_id 
where month(order_date) = 2 and year(order_date) = 2020
group by p.product_id
having unit>=100