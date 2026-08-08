# Write your MySQL query statement below
with t as (
    select *,sum(weight) over(order by turn) as cum_wt
    from Queue
)

select person_name
from t
where cum_wt<=1000
order by turn desc limit 1
