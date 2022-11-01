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

--------------------------------------------------------------
-- Modified by Edward Krueger from
-- Practical SQL: A Beginner's Guide to Storytelling with Data
-- by Anthony DeBarros
--------------------------------------------------------------

-- Listing 1-2: Creating a table named teachers with six columns

CREATE TABLE teachers (
    id bigserial,
    first_name varchar(25),
    last_name varchar(50),
    school varchar(50),
    hire_date date,
    salary numeric
);


--------------------------------------------------------------
-- Modified by Edward Krueger from
-- Practical SQL: A Beginner's Guide to Storytelling with Data
-- by Anthony DeBarros
--------------------------------------------------------------

-- Listing 1-3 Inserting data into the teachers table

INSERT INTO teachers (first_name, last_name, school, hire_date, salary)
VALUES ('Janet', 'Smith', 'F.D. Roosevelt HS', '2011-10-30', 36200),
       ('Lee', 'Reynolds', 'F.D. Roosevelt HS', '1993-05-22', 65000),
       ('Samuel', 'Cole', 'Myers Middle School', '2005-08-01', 43500),
       ('Samantha', 'Bush', 'Myers Middle School', '2011-10-30', 36200),
       ('Betty', 'Diaz', 'Myers Middle School', '2005-08-30', 43500),
       ('Kathleen', 'Roush', 'F.D. Roosevelt HS', '2010-10-22', 38500);
       
      
select hire_date, avg(salary) from teachers group by hire_date

select
	hire_date,
	date_part('month', hire_date),
	date_trunc('month', hire_date)
from
	teachers
	
select
	year::varchar,
	avg(salary)
from
	(
	select
		salary,
		date_part('year', hire_date) as year
	from
		teachers) as sq
	group by year
	
select
	month::varchar,
	avg(salary)
from
	(
	select
		salary,
		date_part('month', hire_date) as month
	from
		teachers) as sq
	group by month
	
select
	month,
	avg(salary)
from
	(
	select
		salary,
		date_trunc('month', hire_date) as month
	from
		teachers) as sq
	group by month
	order by month
	
with cte as (
select
		salary,
		date_trunc('month', hire_date) as month
from
		teachers
)
select
	month,
	avg(salary)
from
	cte
group by
	month
order by
	month
