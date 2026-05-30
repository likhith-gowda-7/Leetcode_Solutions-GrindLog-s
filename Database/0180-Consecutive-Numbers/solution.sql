# Write your MySQL query statement below
with num_neighbours as(
    select num,
    lag(num,1) over() as back,
    lead(num,1) over() as front
    from Logs
)
select distinct num as ConsecutiveNums
from num_neighbours
where back=num and front=num;