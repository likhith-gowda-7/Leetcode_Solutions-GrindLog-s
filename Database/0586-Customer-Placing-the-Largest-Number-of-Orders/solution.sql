# Write your MySQL query statement below
/* Write your T-SQL query statement below */
select customer_number
from Orders
group by customer_number
order by count(*) desc
limit 1;