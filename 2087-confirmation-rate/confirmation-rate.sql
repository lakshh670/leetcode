# Write your MySQL query statement below
select t1.user_id, round(sum(case when t2.action='confirmed' then 1 else 0 end)/count(*),2) as confirmation_rate
from Signups t1
left join Confirmations t2
on t1.user_id=t2.user_id
group by t1.user_id