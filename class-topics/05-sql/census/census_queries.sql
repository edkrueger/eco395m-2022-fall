-- check the total length of each of the datasets
select count(*) from us_counties_2000;
select count(*) from us_counties_2010;

-- check if county_fips is an identifier - its not
select count(*) from (
	select distinct county_fips from  us_counties_2000
) as sq;

select count(*) from (
	select distinct county_fips from  us_counties_2010
) as sq;

-- check if geo_name is an identifier - its not
select count(*) from (
	select distinct geo_name from  us_counties_2000
) as sq;

select count(*) from (
	select distinct geo_name from  us_counties_2010
) as sq;

-- check if state_fips is an identifier - its not
select count(*) from (
	select distinct state_fips from  us_counties_2000
) as sq;

select count(*) from (
	select distinct state_fips from  us_counties_2010
) as sq;

-- investigate the fips
select distinct state_fips from  us_counties_2000
select distinct state_fips from  us_counties_2010
select distinct county_fips from  us_counties_2000
select distinct county_fips from  us_counties_2010

-- look into matching names to state_fips
select distinct on (state_us_abbreviation) state_us_abbreviation, state_fips from  us_counties_2000
select distinct on (state_us_abbreviation) state_us_abbreviation, state_fips from  us_counties_2010

-- check if state_fips and county_fips together is an identifier - it is!
select count(*) from (
	select distinct state_fips, county_fips from  us_counties_2000
) as sq;
select count(*) from (
	select distinct state_fips, county_fips from  us_counties_2010
) as sq;

-- notice that fips are sometimes 0 padded, try to convert to integer to make them match
select county_fips::integer from us_counties_2000 uc 
select county_fips::integer from us_counties_2010 uc 

-- inner join count
select
	count(*)
from
	us_counties_2000 c2000
join us_counties_2010 c2010 on
	c2000.state_fips::int = c2010.state_fips::int and c2000.county_fips::int = c2010.county_fips::int
	
-- outer join count
select
	count(*)
from
	us_counties_2000 c2000
full join us_counties_2010 c2010 on
	c2000.state_fips::int = c2010.state_fips::int and c2000.county_fips::int = c2010.county_fips::int

-- left join count	
select
	count(*)
from
	us_counties_2000 c2000
left join us_counties_2010 c2010 on
	c2000.state_fips::int = c2010.state_fips::int and c2000.county_fips::int = c2010.county_fips::int

-- right join count
select
	count(*)
from
	us_counties_2000 c2000
right join us_counties_2010 c2010 on
	c2000.state_fips::int = c2010.state_fips::int and c2000.county_fips::int = c2010.county_fips::int

-- "anti-join"
select
	*
from
	us_counties_2000 c2000
full join us_counties_2010 c2010 on
	c2000.state_fips::int = c2010.state_fips::int and c2000.county_fips::int = c2010.county_fips::int
where (c2000.state_fips is null or c2000.county_fips is null) or (c2010.state_fips is null or c2010.county_fips is null)

-- cleaned up missing data report
select
	c2000.geo_name, c2000.state_us_abbreviation, c2000.state_fips, c2000.county_fips, c2000.p0010001 as total_population, 0 as missing_2000, 1 as missing_2010
from
	us_counties_2000 c2000
left join us_counties_2010 c2010 on
	c2000.state_fips::int = c2010.state_fips::int and c2000.county_fips::int = c2010.county_fips::int
where c2010.state_fips is null or c2010.county_fips is null
union
select
	c2010.geo_name, c2010.state_us_abbreviation , c2010.state_fips, c2010.county_fips, c2010.p0010001 as total_population, 1 as missing_2000, 0 as missing_2010
from
	us_counties_2000 c2000
right join us_counties_2010 c2010 on
	c2000.state_fips::int = c2010.state_fips::int and c2000.county_fips::int = c2010.county_fips::int
where c2000.state_fips is null or c2000.county_fips is null

-- change in state population with fips
with agg_2000 as (
select
	state_fips::int as state_fips,
	sum(p0010001) as total_population_2000
from
	us_counties_2000 c2000
group by
	state_fips::int
),
agg_2010 as (
select
	state_fips::int as state_fips,
	sum(p0010001) as total_population_2010
from
	us_counties_2010 c2010
group by
	state_fips::int
	)
select
	agg_2000.state_fips,
	total_population_2000,
	total_population_2010,
	total_population_2010 - total_population_2000 as total_population_change
from
	agg_2000
join agg_2010 on
	agg_2000.state_fips = agg_2010.state_fips
order by total_population_change

-- change in state population with abbr
with agg_2000 as (
select
	state_us_abbreviation,
	sum(p0010001) as total_population_2000
from
	us_counties_2000 c2000
group by
	state_us_abbreviation
),
agg_2010 as (
select
	state_us_abbreviation,
	sum(p0010001) as total_population_2010
from
	us_counties_2010 c2010
group by
	state_us_abbreviation
	)
select
	agg_2000.state_us_abbreviation,
	total_population_2000,
	total_population_2010,
	total_population_2010 - total_population_2000 as total_population_change
from
	agg_2000
join agg_2010 on
	agg_2000.state_us_abbreviation = agg_2010.state_us_abbreviation
order by total_population_change

-- change in county population with fips
with agg_2000 as (
select
	state_fips::int as state_fips,
	county_fips::int as county_fips,
	sum(p0010001) as total_population_2000
from
	us_counties_2000 c2000
group by
	state_fips::int, county_fips::int 
),
agg_2010 as (
select
	state_fips::int as state_fips,
	county_fips::int as county_fips,
	sum(p0010001) as total_population_2010
from
	us_counties_2010 c2010
group by
	state_fips::int, county_fips::int
	)
select
	agg_2000.state_fips,
	agg_2000.county_fips,
	total_population_2000,
	total_population_2010,
	total_population_2010 - total_population_2000 as total_population_change
from
	agg_2000
join agg_2010 on
	agg_2000.state_fips = agg_2010.state_fips and agg_2000.county_fips = agg_2010.county_fips
order by total_population_change
