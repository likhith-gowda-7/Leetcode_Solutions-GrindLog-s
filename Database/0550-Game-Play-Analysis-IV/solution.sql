# Write your MySQL query statement below
with User_logins as (
    select player_id,min(event_date) as event_date
    from Activity
    group by player_id
)
select 
round(count(b.event_date)/count(*),2) as fraction
from User_logins a
left join Activity b on
b.player_id=a.player_id
and
b.event_date=(a.event_date + INTERVAL 1 DAY);