select a.reports_to as employee_id,
b.name,
count(a.employee_id) as reports_count,
round(sum(a.age)/count(*),0) as average_age
from Employees a
join Employees b on
b.employee_id=a.reports_to
group by a.reports_to
order by b.employee_id;
