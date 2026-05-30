with details as(
    select *,
    rank() over(PARTITION BY product_id
ORDER BY change_date DESC) as prod_rank
from Products
where change_date<='2019-08-16'
)
select product_id,
new_price as price
from details
where prod_rank=1
Union
select product_id,
10 as price
from Products
where (product_id) not in (select product_id from details)