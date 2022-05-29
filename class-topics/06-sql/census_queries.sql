select
	c2010.geo_name,
	c2000.p0010001 as pop_2000,
	c2010.p0010001 as pop_2010
from
	us_counties_2000 c2000
right join us_counties_2010 c2010 on
	c2000.county_fips = c2010.county_fips
where c2000.p0010001 is Null

with pop_change_table as (select
	c2000.geo_name,
	c2000.state_us_abbreviation,
	c2010.p0010001 - c2000.p0010001 as pop_change
from
	us_counties_2000 c2000
join us_counties_2010 c2010 on
	c2000.county_fips = c2010.county_fips
	)
select * from pop_change_table
order by pop_change

with pop_change_table as (select
	c2000.geo_name,
	c2000.state_us_abbreviation,
	c2010.p0010001 - c2000.p0010001 as pop_change
from
	us_counties_2000 c2000
join us_counties_2010 c2010 on
	c2000.county_fips = c2010.county_fips
	)
select * from pop_change_table
order by pop_change