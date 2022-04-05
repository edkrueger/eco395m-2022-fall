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