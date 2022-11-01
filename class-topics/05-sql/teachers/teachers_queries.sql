select * from teachers;

select * from teachers where hire_date >= '2000-01-01';

select avg(salary) as avg_salary from teachers;

select
    school,
    avg(salary),
    min(salary) as min_salary,
    max(salary) as max_salary
from
    teachers
group by
    school
    
select * from teachers where first_name ilike 's%'

select * from teachers order by salary desc

select * from teachers order by salary desc limit 1

select distinct  school from teachers
