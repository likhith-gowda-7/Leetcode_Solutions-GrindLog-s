# Write your MySQL query statement below
select max(num) as num from (select num,count(*) as n from mynumbers
group by num
having n=1) a
