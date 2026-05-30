# Write your MySQL query statement below
with product_first_year as(
    select product_id,min(year) as min_year
    from Sales
    group by product_id
)
select 
s.product_id,
s.year as first_year,
s.quantity,s.price
from Sales s
where (s.product_id,s.year) in
(select * from product_first_year);