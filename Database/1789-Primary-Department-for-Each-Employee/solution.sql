# Write your MySQL query statement below
with cust_details as(
    select employee_id as emp,count(*) as cnt
    from Employee
    group by employee_id
)
select a.employee_id,a.department_id
from Employee a
join cust_details b on
b.emp=a.employee_id
where b.cnt=1 or (b.cnt>1 and a.primary_flag='Y');