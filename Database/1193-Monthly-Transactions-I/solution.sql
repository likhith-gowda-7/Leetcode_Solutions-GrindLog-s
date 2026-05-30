# Write your MySQL query statement below
-- Extracts 'bcd' from 'abcdef'
SELECT SUBSTRING(trans_date, 1, 7) as month,
country,
count(*) as trans_count,
ifnull(sum(case when state='approved' then 1 end),0) as approved_count,
sum(amount) as trans_total_amount,
ifnull(sum(case when state='approved' then amount end),0) as approved_total_amount
from Transactions
group by month,country;