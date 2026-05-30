# Write your MySQL query statement below
select
p.product_name,sum(o.unit) as unit
from Products p
join Orders o on
o.product_id=p.product_id
    and
    month(o.order_date)=2 and year(o.order_date)=2020
group by o.product_id
having sum(o.unit)>=100;