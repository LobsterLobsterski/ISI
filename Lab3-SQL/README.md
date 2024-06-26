### SQL TUTORIAL

### 2.1. Select  All
``` sql
select * from penguins
```
![pic](images/2_1.png)

### 2.2. Select columns
``` sql
select
    species,
    island,
    sex
from little_penguins;
```
![pic](images/2_2.png)

### 2.3. sorting
``` sql
select
    species,
    sex,
    island
from little_penguins
order by island asc, sex desc;
```
![pic](images/2_3.png)

### 2.4. Limiting Output
``` sql
select
    species,
    sex,
    island
from penguins
order by species, sex, island
limit 10;
```
![pic](images/2_4.png)

### 2.5. Paging Output
``` sql
select
    species,
    sex,
    island
from penguins
order by species, sex, island
limit 10 offset 3;
```
![pic](images/2_5.png)

### 2.6. Removing Duplicates
``` sql
select distinct
    species,
    sex,
    island
from penguins;
```
![pic](images/2_6.png)

### 2.7. Filtering Results
``` sql
select distinct
    species,
    sex,
    island
from penguins
where island = 'Biscoe';
```
![pic](images/2_7.png)

### 2.8. Doing Calculations
``` sql
select
    flipper_length_mm / 10.0,
    body_mass_g / 1000.0
from penguins
limit 3;
```
![pic](images/2_8.png)

### 2.9. Renaming Columns
``` sql
select
    flipper_length_mm / 10.0 as flipper_cm,
    body_mass_g / 1000.0 as weight_kg,
    island as where_found
from penguins
limit 3;
```
![pic](images/2_9.png)

### 2.10. Calculating with Missing Values
``` sql
select
    flipper_length_mm / 10.0 as flipper_cm,
    body_mass_g / 1000.0 as weight_kg,
    island as where_found
from penguins
limit 5;
```
![pic](images/2_10.png)

### 2.11. Null Equality
``` sql
select distinct
    species,
    sex,
    island
from penguins
where island = 'Biscoe';
```
![pic](images/2_11.png)

### 2.12. Null Inequality
``` sql
select distinct
    species,
    sex,
    island
from penguins
where island = 'Biscoe' and sex != 'FEMALE';
```
![pic](images/2_12.png)

### 2.13. Ternary Logic
``` sql
select null = null;

```
![pic](images/2_13.png)


### 2.14. Handling Null Safely
``` sql
select
    species,
    sex,
    island
from penguins
where sex is null;
```
![pic](images/2_14.png)


### 2.15. Aggregating
``` sql
select sum(body_mass_g) as total_mass
from penguins;
```
![pic](images/2_16.png)


### 2.16. Common Aggregation Functions

``` sql
select
    max(bill_length_mm) as longest_bill,
    min(flipper_length_mm) as shortest_flipper,
    avg(bill_length_mm) / avg(bill_depth_mm) as weird_ratio
from penguins;
```
![pic](images/2_17.png)


### 2.17. Counting
``` sql
select
    count(*) as count_star,
    count(sex) as count_specific,
    count(distinct sex) as count_distinct
from penguins;
```
![pic](images/2_18.png)


### 2.18. Grouping

``` sql
select avg(body_mass_g) as average_mass_g
from penguins
group by sex;
```
![pic](images/2_19.png)


### 2.19. Behavior of Unaggregated Columns

``` sql
select
    sex,
    avg(body_mass_g) as average_mass_g
from penguins
group by sex;
```
![pic](images/2_20.png)


### 2.20. Arbitrary Choice in Aggregation

``` sql
select
    sex,
    body_mass_g
from penguins
group by sex;
```
![pic](images/2_21.png)

### 2.21. Filtering Aggregated Values

``` sql
select
    sex,
    avg(body_mass_g) as average_mass_g
from penguins
group by sex
having average_mass_g > 4000.0;
```
![pic](images/2_22.png)
### 2.22. Readable Output

``` sql
select
    sex,
    round(avg(body_mass_g), 1) as average_mass_g
from penguins
group by sex
having average_mass_g > 4000.0;
```
![pic](images/2_23.png)
### 2.23. Filtering Aggregate Inputs

``` sql
select
    sex,
    round(
        avg(body_mass_g) filter (where body_mass_g < 4000.0),
        1
    ) as average_mass_g
from penguins
group by sex;
```
![pic](images/2_24.png)
### 2.24. Creating In-memory Database, Python scripts

``` sql
CHECK THE LAST SECTION FOR PYTHON
```
![pic](images/2_25.png)
### 2.25. Combining Information

``` sql
select *
from penguins cross join little_penguins;
```
![pic](images/2_26.png)
### 2.26. Inner Join

``` sql
select *
from penguins inner join little_penguins
    on penguins.species = little_penguins.species;
```
![pic](images/2_27.png)
### 2.27. Aggregating Joined Data

``` sql
select
    penguins.island,
    sum(little_penguins.bill_length_mm) as bill_length
from penguins inner join little_penguins
    on penguins.species = little_penguins.species
group by penguins.species;
```
![pic](images/2_28.png)
### 2.28. Left Join

``` sql
select *
from penguins left join little_penguins
    on penguins.species = little_penguins.species;
```
![pic](images/2_29.png)
### 2.29. Coalescing Values

``` sql
select
    penguins.island,
    coalesce(sum(little_penguins.bill_length_mm), 0.0) as bill_length
from penguins left join little_penguins
    on penguins.species = little_penguins.species
group by penguins.species;
```
![pic](images/2_29.png)
### 2.30. Full Outer Join

``` sql
create table size (
    s text not null
);
insert into size values ('light'), ('heavy');

create table weight (
    w text not null
);

select * from size outer join weight;
```
![pic](images/2_30.png)


### 3.1. Negating Incorrectly

``` sql
select distinct island
from penguins
where species != 'Gentoo';
```
![pic](images/3_1.png)


### 3.2. Set Membership

``` sql
select *
from penguins
where species not in ('Gentoo', 'Adelie');
```
![pic](images/3_2.png)


### 3.3. Subqueries
``` sql
select distinct island
from penguins
where island not in (
    select distinct island
    from penguins
    where species = 'Gentoo'
);
```
![pic](images/3_3.png)


### 3.4. Defining a Primary Key

``` sql
create table lab_equipment (
    size real not null,
    color text not null,
    num integer not null,
    primary key (size, color)
);

insert into lab_equipment values
(1.5, 'blue', 2),
(1.5, 'green', 1),
(2.5, 'blue', 1);

select * from lab_equipment;

insert into lab_equipment values
(1.5, 'green', 2);
```
![pic](images/3_4.png)


### 3.5. Autoincrementing and Primary Keys

``` sql
create table person (
    ident integer primary key autoincrement,
    name text not null
);
insert into person values
(null, 'mik'),
(null, 'po'),
(null, 'tay');
select * from person;
insert into person values (1, 'prevented');
```
![pic](images/3_5.png)


### 3.6. Internal Tables

``` sql
select * from sqlite_sequence;

```
![pic](images/3_6.png)


### 3.7. Altering Tables

``` sql
alter table little_penguins
add ident integer not null default -1;

update little_penguins
set ident = 1
where species = 'Gentoo';

update little_penguins
set ident = 2
where species = 'Adelie';

select * from little_penguins;
```
![pic](images/3_7.png)


### 3.8. Creating New Tables from Old

``` sql
create table new_work (
    person_id integer not null,
    penguin_id integer not null,
    foreign key (person_id) references person (ident),
    foreign key (penguin_id) references little_penguins (ident)
);

insert into new_work
select
    person.ident as person_id,
    little_penguins.ident as penguin_id
from
    (person inner join penguins on person.name != penguins.species)
    inner join little_penguins on little_penguins.species = penguins.species;
select * from new_work;
```
![pic](images/3_8.png)


### 3.9. Removing Tables

``` sql
CREATE TABLE job (
    ident integer primary key autoincrement,
    name text not null,
    billable real not null
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE person (
    ident integer primary key autoincrement,
    name text not null
);
CREATE TABLE IF NOT EXISTS "work" (
    person_id integer not null,
    job_id integer not null,
    foreign key(person_id) references person(ident),
    foreign key(job_id) references job(ident)
);
```
![pic](images/3_9.png)


### 3.10. Comparing Individual Values to Aggregates

``` sql
select body_mass_g
from penguins
where
    body_mass_g > (
        select avg(body_mass_g)
        from penguins
    )
limit 5;
```
![pic](images/3_10.png)


### 3.11. Comparing Individual Values to Aggregates Within Groups

``` sql
select
    penguins.species,
    penguins.body_mass_g,
    round(averaged.avg_mass_g, 1) as avg_mass_g
from penguins inner join (
    select
        species,
        avg(body_mass_g) as avg_mass_g
    from penguins
    group by species
) as averaged
    on penguins.species = averaged.species
where penguins.body_mass_g > averaged.avg_mass_g
limit 5;
```
![pic](images/3_11.png)


### 3.12. Common Table Expressions

``` sql
with grouped as (
    select
        species,
        avg(body_mass_g) as avg_mass_g
    from penguins
    group by species
)

select
    penguins.species,
    penguins.body_mass_g,
    round(grouped.avg_mass_g, 1) as avg_mass_g
from penguins inner join grouped
where penguins.body_mass_g > grouped.avg_mass_g
limit 5;
```
![pic](images/3_12.png)


### 3.13. Explaining Query Plans

``` sql
explain query plan
select
    species,
    avg(body_mass_g)
from penguins
group by species;
```
![pic](images/3_13.png)


### 3.14. Enumerating Rows

``` sql
select
    rowid,
    species,
    island
from penguins
limit 5;
```
![pic](images/3_14.png)


### 3.15. Conditionals

``` sql
with sized_penguins as (
    select
        species,
        iif(
            body_mass_g < 3500,
            'small',
            'large'
        ) as size
    from penguins
    where body_mass_g is not null
)

select
    species,
    size,
    count(*) as num
from sized_penguins
group by species, size
order by species, num;
```
![pic](images/3_15.png)


### 3.16. Selecting a Case

``` sql
with sized_penguins as (
    select
        species,
        case
            when body_mass_g < 3500 then 'small'
            when body_mass_g < 5000 then 'medium'
            else 'large'
        end as size
    from penguins
    where body_mass_g is not null
)

select
    species,
    size,
    count(*) as num
from sized_penguins
group by species, size
order by species, num;
```
![pic](images/3_16.png)


### 3.17. Checking a Range

``` sql
with sized_penguins as (
    select
        species,
        case
            when body_mass_g between 3500 and 5000 then 'normal'
            else 'abnormal'
        end as size
    from penguins
    where body_mass_g is not null
)

select
    species,
    size,
    count(*) as num
from sized_penguins
group by species, size
order by species, num;
```
![pic](images/3_17.png)


### 3.18. Pattern Matching

``` sql
select
    species,
    island
from penguins
where species like '%e%';
```
![pic](images/3_18.png)


### 3.19. Selecting First and Last Rows

``` sql
select * from (
    select * from (select * from experiment order by started asc limit 5)
    union all
    select * from (select * from experiment order by started desc limit 5)
)
order by started asc;
```
![pic](images/3_19.png)


### 3.20. Intersection
``` sql
select
    species,
    island,
    sex
from penguins
where island = 'Torgersen'
intersect
select
    species,
    island,
    sex
    from penguins
where bill_length_mm < 50;
```
![pic](images/3_20.png)


### 3.21. Exclusion
``` sql
select
    species,
    island,
    sex
from penguins
where island = 'Torgersen'
except
select
    species,
    island,
    sex
    from penguins
where bill_length_mm < 30;
```
![pic](images/3_21.png)


### 3.22. Random Numbers and Why Not

``` sql
with decorated as (
    select random() as rand,
    personal || ' ' || family as name
    from staff
)

select
    rand,
    abs(rand) % 10 as selector,
    name
from decorated
where selector < 5;
```
![pic](images/3_22.png)


### 3.23. Creating an Index

``` sql
explain query plan
select filename
from plate
where filename like '%07%';

create index plate_file on plate(filename);

explain query plan
select filename
from plate
where filename like '%07%';
```
![pic](images/3_23.png)


### 3.24. Generating Sequences

``` sql
select value from generate_series(1, 5);

```
![pic](images/3_24.png)


### 3.25. Generating Sequences of Dates

``` sql
create table temp (
    num integer not null
);
insert into temp values (1), (5);
select value from generate_series (
    (select min(num) from temp),
    (select max(num) from temp)
);
```
![pic](images/3_25.png)


### 3.26. Counting Experiments Started per Day Without Gaps

``` sql
with
-- complete sequence of days with 0 as placeholder for number of experiments
all_days as (
    select
        date((select julianday(min(started)) from experiment) + value) as some_day,
        0 as zeroes
    from (
        select value from generate_series(
            (select 0),
            (select count(*) - 1 from experiment)
        )
    )
),

-- sequence of actual days with actual number of experiments started
actual_days as (
    select
        started,
        count(started) as num_exp
    from experiment
    group by started
)

-- combined by joining on day and taking actual number (if available) or zero
select
    all_days.some_day as day,
    coalesce(actual_days.num_exp, all_days.zeroes) as num_exp
from
    all_days left join actual_days on all_days.some_day = actual_days.started
limit 5;
```
![pic](images/3_26.png)


### 3.27. Self Join

``` sql
with person as (
    select
        ident,
        personal || ' ' || family as name
    from staff
)

select
    left_person.name,
    right_person.name
from person as left_person inner join person as right_person
limit 10;
```
![pic](images/3_27.png)


### 3.28. Generating Unique Pairs

``` sql
with person as (
    select
        ident,
        personal || ' ' || family as name
    from staff
)

select
    left_person.name,
    right_person.name
from person as left_person inner join person as right_person
on left_person.ident < right_person.ident
where left_person.ident <= 4 and right_person.ident <= 4;
```
![pic](images/3_28.png)


### 3.29. Filtering Pairs

``` sql
with
person as (
    select
        ident,
        personal || ' ' || family as name
    from staff
),

together as (
    select
        left_perf.staff as left_staff,
        right_perf.staff as right_staff
    from performed as left_perf inner join performed as right_perf
        on left_perf.experiment = right_perf.experiment
    where left_staff < right_staff
)

select
    left_person.name as person_1,
    right_person.name as person_2
from person as left_person inner join person as right_person join together
    on left_person.ident = left_staff and right_person.ident = right_staff;
```
![pic](images/3_29.png)


### 3.30. Existence and Correlated Subqueries

``` sql
select
    name,
    building
from department
where
    exists (
        select 1
        from staff
        where dept = department.ident
    )
order by name;
```
![pic](images/3_30.png)


### 3.31. Nonexistence

``` sql
select
    name,
    building
from department
where
    not exists (
        select 1
        from staff
        where dept = department.ident
    )
order by name;
```
![pic](images/3_31.png)


### 3.32. Avoiding Correlated Subqueries

``` sql
select distinct
    department.name as name,
    department.building as building
from department inner join staff
    on department.ident = staff.dept
order by name;
```
![pic](images/3_32.png)


### 3.33. Lead and Lag

``` sql
with ym_num as (
    select
        strftime('%Y-%m', started) as ym,
        count(*) as num
    from experiment
    group by ym
)

select
    ym,
    lag(num) over (order by ym) as prev_num,
    num,
    lead(num) over (order by ym) as next_num
from ym_num
order by ym;
```
![pic](images/3_33.png)


### 3.34. Windowing Functions

``` sql
with ym_num as (
    select
        strftime('%Y-%m', started) as ym,
        count(*) as num
    from experiment
    group by ym
)

select
    ym,
    num,
    sum(num) over (order by ym) as num_done,
    (sum(num) over (order by ym) * 1.00) / (select sum(num) from ym_num) as completed_progress,
    cume_dist() over (order by ym) as linear_progress
from ym_num
order by ym;
```
![pic](images/3_34.png)


### 3.35. Explaining Another Query Plan

``` sql
explain query plan
with ym_num as (
    select
        strftime('%Y-%m', started) as ym,
        count(*) as num
    from experiment
    group by ym
)
select
    ym,
    num,
    sum(num) over (order by ym) as num_done,
    cume_dist() over (order by ym) as progress
from ym_num
order by ym;
```
![pic](images/3_35.png)


### 3.36. Partitioned Windows

``` sql
with y_m_num as (
    select
        strftime('%Y', started) as year,
        strftime('%m', started) as month,
        count(*) as num
    from experiment
    group by year, month
)

select
    year,
    month,
    num,
    sum(num) over (partition by year order by month) as num_done
from y_m_num
order by year, month;
```
![pic](images/3_36.png)


### 4.1. Blobs
``` sql
create table images (
    name text not null,
    content blob
);

insert into images (name, content) values
('biohazard', readfile('img/biohazard.png')),
('crush', readfile('img/crush.png')),
('fire', readfile('img/fire.png')),
('radioactive', readfile('img/radioactive.png')),
('tripping', readfile('img/tripping.png'));

select
    name,
    length(content)
from images;
```
![pic](images/4_1.png)


### 4.2. Yet Another Database

``` sql
.schema
```
![pic](images/4_2.png)


### 4.3. Storing JSON

``` sql
select * from machine;

```
![pic](images/4_3.png)


### 4.4. Select Fields from JSON

``` sql
select
    details->'$.acquired' as single_arrow,
    details->>'$.acquired' as double_arrow
from machine;
```
![pic](images/4_4.png)


### 4.5. JSON Array Access

``` sql
select
    ident,
    json_array_length(log->'$') as length,
    log->'$[0]' as first
from usage;
```
![pic](images/4_5.png)


### 4.6. Unpacking JSON Arrays

``` sql
select
    ident,
    json_each.key as key,
    json_each.value as value
from usage, json_each(usage.log)
limit 10;
```
![pic](images/4_6.png)


### 4.7. Selecting the Last Element of an Array

``` sql
select
    ident,
    log->'$[#-1].machine' as final
from usage
limit 5;
```
![pic](images/4_7.png)


### 4.8. Modifying JSON

``` sql
select
    ident,
    name,
    json_set(details, '$.sold', json_quote('2024-01-25')) as updated
from machine;
```
![pic](images/4_8.png)


### 4.9. Refreshing the Penguins Database

``` sql
select
    species,
    count(*) as num
from penguins
group by species;
```
![pic](images/4_9.png)


### 4.10. Tombstones

``` sql
alter table penguins
add active integer not null default 1;

update penguins
set active = iif(species = 'Adelie', 0, 1);
```
``` sql
select
    species,
    count(*) as num
from penguins
where active
group by species;
```
![pic](images/4_10.png)

### 4.11. Importing CSV Data

``` sql
drop table if exists penguins;
.mode csv penguins
.import misc/penguins.csv penguins
update penguins set species = null where species = '';
update penguins set island = null where island = '';
update penguins set bill_length_mm = null where bill_length_mm = '';
update penguins set bill_depth_mm = null where bill_depth_mm = '';
update penguins set flipper_length_mm = null where flipper_length_mm = '';
update penguins set body_mass_g = null where body_mass_g = '';
update penguins set sex = null where sex = '';
```
![pic](images/4_11.png)


### 4.12. Views

``` sql
create view if not exists
active_penguins (
    species,
    island,
    bill_length_mm,
    bill_depth_mm,
    flipper_length_mm,
    body_mass_g,
    sex
) as
select
    species,
    island,
    bill_length_mm,
    bill_depth_mm,
    flipper_length_mm,
    body_mass_g,
    sex
from penguins
where active;

select
    species,
    count(*) as num
from active_penguins
group by species;
```
![pic](images/4_12.png)


### 4.13. Hours Reminder

``` sql
create table job (
    name text not null,
    billable real not null
);
insert into job values
('calibrate', 1.5),
('clean', 0.5);
select * from job;
```
![pic](images/4_13.png)


### 4.14. Adding Checks

``` sql
drop table job;
create table job (
    name text not null,
    billable real not null,
    check (billable > 0.0)
);
insert into job values ('calibrate', 1.5);
insert into job values ('reset', -0.5);
select * from job;
```
![pic](images/4_14.png)


### 4.15. Transactions

``` sql
drop table job;
create table job (
    name text not null,
    billable real not null,
    check (billable > 0.0)
);

insert into job values ('calibrate', 1.5);

begin transaction;
insert into job values ('clean', 0.5);
rollback;

select * from job;
```
![pic](images/4_15.png)


### 4.16. Rollback in Constraints

``` sql
drop table job;
create table job (
    name text not null,
    billable real not null,
    check (billable > 0.0) on conflict rollback
);

insert into job values
    ('calibrate', 1.5);
insert into job values
    ('clean', 0.5),
    ('reset', -0.5);

select * from job;
```
![pic](images/4_16.png)


### 4.17. Rollback in Statements

``` sql
drop table job;
create table job (
    name text not null,
    billable real not null,
    check (billable > 0.0)
);

insert or rollback into job values
('calibrate', 1.5);
insert or rollback into job values
('clean', 0.5),
('reset', -0.5);

select * from job;
```
![pic](images/4_17.png)


### 4.18. Upsert
``` sql
create table jobs_done (
    person text unique,
    num integer default 0
);

insert into jobs_done values
('zia', 1);
.print 'after first'
select * from jobs_done;
.print


insert into jobs_done values
('zia', 1);
.print 'after failed'
select * from jobs_done;

insert into jobs_done values
('zia', 1)
on conflict(person) do update set num = num + 1;
.print '/nafter upsert'
select * from jobs_done;
```
![pic](images/4_18.png)


### 4.19. Creating Triggers

``` sql
-- Track hours of lab work.
create table job (
    person text not null,
    reported real not null check (reported >= 0.0)
);

-- Explicitly store per-person total rather than using sum().
create table total (
    person text unique not null,
    hours real
);

-- Initialize totals.
insert into total values
('gene', 0.0),
('august', 0.0);

-- Define a trigger.
create trigger total_trigger
before insert on job
begin
    -- Check that the person exists.
    select case
        when not exists (select 1 from total where person = new.person)
        then raise(rollback, 'Unknown person ')
    end;
    -- Update their total hours (or fail if non-negative constraint violated).
    update total
    set hours = hours + new.reported
    where total.person = new.person;
end;
```
![pic](images/4_19.png)


### 4.20. Trigger Not Firing

``` sql
insert into job values
('gene', 1.5),
('august', 0.5),
('gene', 1.0);
```
![pic](images/4_20.png)


### 4.21. Trigger Firing

``` sql
insert into job values
('gene', 1.0),
('august', -1.0);
```
![pic](images/4_21.png)


### 4.22. Representing Graphs

``` sql
create table lineage (
    parent text not null,
    child text not null
);
insert into lineage values
('Arturo', 'Clemente'),
('Darío', 'Clemente'),
('Clemente', 'Homero'),
('Clemente', 'Ivonne'),
('Ivonne', 'Lourdes'),
('Soledad', 'Lourdes'),
('Lourdes', 'Santiago');
```
```sql
select * from lineage;
```
![pic](images/4_22.png)


### 4.23. Recursive Queries

``` sql
with recursive descendent as (
    select
        'Clemente' as person,
        0 as generations
    union all
    select
        lineage.child as person,
        descendent.generations + 1 as generations
    from descendent inner join lineage
        on descendent.person = lineage.parent
)

select
    person,
    generations
from descendent;
```
![pic](images/4_23.png)


### 4.24. Bidirectional Contacts

``` sql
create temporary table bi_contact (
    left text,
    right text
);

insert into bi_contact
select
    left, right from contact
    union all
    select right, left from contact
;
```
![pic](images/4_24.png)


### 4.25. Updating Group Identifiers

``` sql
select
    left.name as left_name,
    left.ident as left_ident,
    right.name as right_name,
    right.ident as right_ident,
    min(left.ident, right.ident) as new_ident
from
    (person as left join bi_contact on left.name = bi_contact.left)
    join person as right on bi_contact.right = right.name;
```
![pic](images/4_25.png)


### 4.26. Recursive Labeling

``` sql
with recursive labeled as (
    select
        person.name as name,
        person.ident as label
    from
        person
    union -- not 'union all'
    select
        person.name as name,
        labeled.label as label
    from
        (person join bi_contact on person.name = bi_contact.left)
        join labeled on bi_contact.right = labeled.name
    where labeled.label < person.ident
)
select name, min(label) as group_id
from labeled
group by name
order by label, name;
```
![pic](images/4_26.png)


### 5.1. Querying from Python

``` python
import sqlite3

db_path = 'C:/Users/tomas/Desktop/szkola/ISI/Lab3-SQL/db/penguins.db'
connection = sqlite3.connect(db_path)
cursor = connection.execute("select count(*) from penguins;")
rows = cursor.fetchall()
print(rows)
```
![pic](images/5_1.png)


### 5.2. Incremental Fetch

``` python
import sqlite3

db_path = 'C:/Users/tomas/Desktop/szkola/ISI/Lab3-SQL/db/penguins.db'
connection = sqlite3.connect(db_path)
cursor = connection.cursor()
cursor = cursor.execute("select species, island from penguins limit 5;")
while row := cursor.fetchone():
    print(row)
```
![pic](images/5_2.png)


### 5.3. Insert, Delete, and All That

``` python
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("create table example(num integer);")

cursor.execute("insert into example values (10), (20);")
print("after insertion", cursor.execute("select * from example;").fetchall())

cursor.execute("delete from example where num < 15;")
print("after deletion", cursor.execute("select * from example;").fetchall())
```
![pic](images/5_3.png)


### 5.4. Interpolating Values

``` python
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("create table example(num integer);")

cursor.executemany("insert into example values (?);", [(10,), (20,)])
print("after insertion", cursor.execute("select * from example;").fetchall())
```
![pic](images/5_4.png)


### 5.5. Script Execution

``` python
import sqlite3

SETUP = """\
drop table if exists example;
create table example(num integer);
insert into example values (10), (20);
"""

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.executescript(SETUP)
print("after insertion", cursor.execute("select * from example;").fetchall())
```
![pic](images/5_5.png)


### 5.6. SQLite Exceptions in Python

``` python
import sqlite3

SETUP = """\
create table example(num integer check(num > 0));
insert into example values (10);
insert into example values (-1);
insert into example values (20);
"""

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
try:
    cursor.executescript(SETUP)
except sqlite3.Error as exc:
    print(f"SQLite exception: {exc}")
print("after execution", cursor.execute("select * from example;").fetchall())
```
![pic](images/5_6.png)


### 5.7. Python in SQLite

``` python
import sqlite3

SETUP = """\
create table example(num integer);
insert into example values (-10), (10), (20), (30);
"""


def clip(value):
    if value < 0:
        return 0
    if value > 20:
        return 20
    return value


connection = sqlite3.connect(":memory:")
connection.create_function("clip", 1, clip)
cursor = connection.cursor()
cursor.executescript(SETUP)
for row in cursor.execute("select num, clip(num) from example;").fetchall():
    print(row)
```
![pic](images/5_7.png)


### 5.8. Handling Dates and Times

``` python
from datetime import date
import sqlite3


# Convert date to ISO-formatted string when writing to database
def _adapt_date_iso(val):
    return val.isoformat()


sqlite3.register_adapter(date, _adapt_date_iso)


# Convert ISO-formatted string to date when reading from database
def _convert_date(val):
    return date.fromisoformat(val.decode())


sqlite3.register_converter("date", _convert_date)

SETUP = """\
create table events(
    happened date not null,
    description text not null
);
"""

connection = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cursor = connection.cursor()
cursor.execute(SETUP)

cursor.executemany(
    "insert into events values (?, ?);",
    [(date(2024, 1, 10), "started tutorial"), (date(2024, 1, 29), "finished tutorial")],
)

for row in cursor.execute("select * from events;").fetchall():
    print(row)
```
![pic](images/5_8.png)


### 5.9. Pandas and SQL

``` python
import pandas as pd
import sqlite3
import sys

db_path = 'C:/Users/tomas/Desktop/szkola/ISI/Lab3-SQL/db/penguins.db'
connection = sqlite3.connect(db_path)
query = "select species, count(*) as num from penguins group by species;"
df = pd.read_sql(query, connection)
print(df)
```
![pic](images/5_9.png)


### 5.10. Polars and SQL

``` python
import polars as pl
import sys

db_path = 'C:/Users/tomas/Desktop/szkola/ISI/Lab3-SQL/db/penguins.db'
uri = "sqlite:///{db_path}"
query = "select species, count(*) as num from penguins group by species;"
df = pl.read_database_uri(query, uri, engine="adbc")
print(df)
```
![pic](images/5_10.png)


### 5.11. Object-Relational Mappers

``` python
from sqlmodel import Field, Session, SQLModel, create_engine, select
import sys


class Department(SQLModel, table=True):
    ident: str = Field(default=None, primary_key=True)
    name: str
    building: str


db_uri = "sqlite:///C:/Users/tomas/Desktop/szkola/ISI/Lab3-SQL/db/assays.db"
engine = create_engine(db_uri)
with Session(engine) as session:
    statement = select(Department)
    for result in session.exec(statement).all():
        print(result)
```
![pic](images/5_11.png)


### 5.12. Relations with ORMs

```python
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Staff(SQLModel, table=True):
    ident: str = Field(default=None, primary_key=True)
    personal: str
    family: str
    dept: Optional[str] = Field(default=None, foreign_key="department.ident")
    age: int

class Department(SQLModel, table=True):
    ident: str = Field(default=None, primary_key=True)
    name: str
    building: str

db_uri = "sqlite:///C:/Users/tomas/Desktop/szkola/ISI/Lab3-SQL/db/assays.db"
engine = create_engine(db_uri)
SQLModel.metadata.create_all(engine)
with Session(engine) as session:
    statement = select(Department, Staff).where(Staff.dept == Department.ident)
    for dept, staff in session.exec(statement):
        print(f"{dept.name}: {staff.personal} {staff.family}")
```

![pic](images/5_12.png)

![THATS ALL FOLKS](https://i1.sndcdn.com/artworks-000605731930-1ql21b-t500x500.jpg)
