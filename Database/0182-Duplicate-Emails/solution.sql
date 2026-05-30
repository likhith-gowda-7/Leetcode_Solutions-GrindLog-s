# Write your MySQL query statement below
with emails as (
    select email,count(*) as email_count from Person
    group by email
)
select email as Email from emails
where email_count>1;