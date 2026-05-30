# Write your MySQL query statement below
with person_sum as(
select person_name,sum(weight) over (order by turn) as total
from Queue
)
select person_name from person_sum
where total<=1000
order by total desc limit 1;