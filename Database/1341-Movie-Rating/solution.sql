# Write your MySQL query statement below
(select u.name as results
from Users u
join MovieRating mr
on mr.user_id=u.user_id
group by u.user_id,u.name
order by count(*) desc,u.name asc
limit 1)
Union ALL
(select m.title
from Movies m
join MovieRating mr1
on mr1.movie_id=m.movie_id
WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
group by m.movie_id,m.title
order by avg(mr1.rating) desc,m.title asc limit 1);