# Write your MySQL query statement below
select *,
if((y+z)>x and (x+z)>y and (x+y)>z,"Yes","No") as triangle
from Triangle
