### SQL TUTORIAL

### 2.1. Select  All
``` sql
select * from penguins
```
![pic](images\2_1.png)

### 2.2. Select columns
``` sql
select
    species,
    island,
    sex
from little_penguins;
```
![pic](images\2_2.png)

### 2.3. sorting
``` sql
select
    species,
    sex,
    island
from little_penguins
order by island asc, sex desc;
```
![pic](images\2_3.png)

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
![pic](images\2_4.png)

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
![pic](images\2_5.png)

### 2.6. Removing Duplicates
``` sql
select distinct
    species,
    sex,
    island
from penguins;
```
![pic](images\2_6.png)

### 2.7. Filtering Results
``` sql
select distinct
    species,
    sex,
    island
from penguins
where island = 'Biscoe';
```
![pic](images\2_7.png)

### 2.8. Doing Calculations
``` sql
select
    flipper_length_mm / 10.0,
    body_mass_g / 1000.0
from penguins
limit 3;
```
![pic](images\2_8.png)

### 2.9. Renaming Columns
``` sql
select
    flipper_length_mm / 10.0 as flipper_cm,
    body_mass_g / 1000.0 as weight_kg,
    island as where_found
from penguins
limit 3;
```
![pic](images\2_9.png)

### 2.10. Calculating with Missing Values
``` sql
select
    flipper_length_mm / 10.0 as flipper_cm,
    body_mass_g / 1000.0 as weight_kg,
    island as where_found
from penguins
limit 5;
```
![pic](images\2_10.png)

### 2.11. Null Equality
``` sql
sqllllll
```
![pic](images\2_11.png)

### 2.12. Null Inequality
``` sql
sqllllll
```
![pic](images\2_12.png)

### 2.12. Ternary Logic
``` sql
sqllllll
```
![pic](images\2_13.png)


### 2.13. Handling Null Safely
``` sql
sqllllll
```
![pic](images\2_14.png)


### 2.14. Check Understanding
``` sql
sqllllll
```
![pic](images\2_15.png)


### 2.15. Aggregating
``` sql
sqllllll
```
![pic](images\2_16.png)


### 2.16. Common Aggregation Functions

``` sql
sqllllll
```
![pic](images\2_17.png)


### 2.17. Counting
``` sql
sqllllll
```
![pic](images\2_18.png)


### 2.18. Grouping

``` sql
sqllllll
```
![pic](images\2_19.png)


### 2.19. Behavior of Unaggregated Columns

``` sql
sqllllll
```
![pic](images\2_20.png)


### 2.20. Arbitrary Choice in Aggregation

``` sql
sqllllll
```
![pic](images\2_21.png)

### 2.21. Filtering Aggregated Values

``` sql
sqllllll
```
![pic](images\2_22.png)
### 2.22. Readable Output

``` sql
sqllllll
```
![pic](images\2_23.png)
### 2.23. Filtering Aggregate Inputs

``` sql
sqllllll
```
![pic](images\2_24.png)
### 2.24. Creating In-memory Database, Python scripts

``` sql
sqllllll
```
![pic](images\2_25.png)
### 2.25. Combining Information

``` sql
sqllllll
```
![pic](images\2_26.png)
### 2.26. Inner Join

``` sql
sqllllll
```
![pic](images\2_27.png)
### 2.27. Aggregating Joined Data

``` sql
sqllllll
```
![pic](images\2_28.png)
### 2.28. Left Join

``` sql
sqllllll
```
![pic](images\2_29.png)
### 2.29. Coalescing Values

``` sql
sqllllll
```
![pic](images\2_30.png)
### 2.30. Full Outer Join

``` sql
sqllllll
```
![pic](images\2_0.png)


### 3.1. Negating Incorrectly

``` sql
sqllllll
```
![pic](images\3_1.png)


### 3.2. Set Membership

``` sql
sqllllll
```
![pic](images\3_2.png)


### 3.3. Subqueries
``` sql
sqllllll
```
![pic](images\3_3.png)


### 3.4. Defining a Primary Key

``` sql
sqllllll
```
![pic](images\3_4.png)


### 3.5. Autoincrementing and Primary Keys

``` sql
sqllllll
```
![pic](images\3_5.png)


### 3.6. Internal Tables

``` sql
sqllllll
```
![pic](images\3_6.png)


### 3.7. Altering Tables

``` sql
sqllllll
```
![pic](images\3_7.png)


### 3.8. Creating New Tables from Old

``` sql
sqllllll
```
![pic](images\3_8.png)


### 3.9. Removing Tables

``` sql
sqllllll
```
![pic](images\3_9.png)


### 3.10. Comparing Individual Values to Aggregates

``` sql
sqllllll
```
![pic](images\3_10.png)


### 3.11. Comparing Individual Values to Aggregates Within Groups

``` sql
sqllllll
```
![pic](images\3_11.png)


### 3.12. Common Table Expressions

``` sql
sqllllll
```
![pic](images\3_12.png)


### 3.13. Explaining Query Plans

``` sql
sqllllll
```
![pic](images\3_13.png)


### 3.14. Enumerating Rows

``` sql
sqllllll
```
![pic](images\3_14.png)


### 3.15. Conditionals

``` sql
sqllllll
```
![pic](images\3_15.png)


### 3.16. Selecting a Case

``` sql
sqllllll
```
![pic](images\3_16.png)


### 3.17. Checking a Range

``` sql
sqllllll
```
![pic](images\3_17.png)


### 3.18. Pattern Matching

``` sql
sqllllll
```
![pic](images\3_18.png)


### 3.19. Selecting First and Last Rows

``` sql
sqllllll
```
![pic](images\3_19.png)


### 3.20. Intersection
``` sql
sqllllll
```
![pic](images\3_20.png)


### 3.21. Exclusion
``` sql
sqllllll
```
![pic](images\3_21.png)


### 3.22. Random Numbers and Why Not

``` sql
sqllllll
```
![pic](images\3_22.png)


### 3.23. Creating an Index

``` sql
sqllllll
```
![pic](images\3_23.png)


### 3.24. Generating Sequences

``` sql
sqllllll
```
![pic](images\3_24.png)


### 3.25. Generating Sequences of Dates

``` sql
sqllllll
```
![pic](images\3_25.png)


### 3.26. Counting Experiments Started per Day Without Gaps

``` sql
sqllllll
```
![pic](images\3_26.png)


### 3.27. Self Join

``` sql
sqllllll
```
![pic](images\3_27.png)


### 3.28. Generating Unique Pairs

``` sql
sqllllll
```
![pic](images\3_28.png)


### 3.29. Filtering Pairs

``` sql
sqllllll
```
![pic](images\3_29.png)


### 3.30. Existence and Correlated Subqueries

``` sql
sqllllll
```
![pic](images\3_30.png)


### 3.31. Nonexistence

``` sql
sqllllll
```
![pic](images\3_31.png)


### 3.32. Avoiding Correlated Subqueries

``` sql
sqllllll
```
![pic](images\3_32.png)


### 3.33. Lead and Lag

``` sql
sqllllll
```
![pic](images\3_33.png)


### 3.34. Windowing Functions

``` sql
sqllllll
```
![pic](images\3_34.png)


### 3.35. Explaining Another Query Plan

``` sql
sqllllll
```
![pic](images\3_35.png)


### 3.36. Partitioned Windows

``` sql
sqllllll
```
![pic](images\3_36.png)


### 4.1. Blobs
``` sql
sqllllll
```
![pic](images\4_1.png)


### 4.2. Yet Another Database

``` sql
sqllllll
```
![pic](images\4_2.png)


### 4.3. Storing JSON

``` sql
sqllllll
```
![pic](images\4_3.png)


### 4.4. Select Fields from JSON

``` sql
sqllllll
```
![pic](images\4_4.png)


### 4.5. JSON Array Access

``` sql
sqllllll
```
![pic](images\4_5.png)


### 4.6. Unpacking JSON Arrays

``` sql
sqllllll
```
![pic](images\4_6.png)


### 4.7. Selecting the Last Element of an Array

``` sql
sqllllll
```
![pic](images\4_7.png)


### 4.8. Modifying JSON

``` sql
sqllllll
```
![pic](images\4_8.png)


### 4.9. Refreshing the Penguins Database

``` sql
sqllllll
```
![pic](images\4_9.png)


### 4.10. Tombstones

``` sql
sqllllll
```
![pic](images\4_10.png)


### 4.11. Importing CSV Data

``` sql
sqllllll
```
![pic](images\4_11.png)


### 4.12. Views

``` sql
sqllllll
```
![pic](images\4_12.png)


### 4.13. Hours Reminder

``` sql
sqllllll
```
![pic](images\4_13.png)


### 4.14. Adding Checks

``` sql
sqllllll
```
![pic](images\4_14.png)


### 4.15. Transactions

``` sql
sqllllll
```
![pic](images\4_15.png)


### 4.16. Rollback in Constraints

``` sql
sqllllll
```
![pic](images\4_16.png)


### 4.17. Rollback in Statements

``` sql
sqllllll
```
![pic](images\4_17.png)


### 4.18. Upsert
``` sql
sqllllll
```
![pic](images\4_18.png)


### 4.19. Creating Triggers

``` sql
sqllllll
```
![pic](images\4_19.png)


### 4.20. Trigger Not Firing

``` sql
sqllllll
```
![pic](images\4_20.png)


### 4.21. Trigger Firing

``` sql
sqllllll
```
![pic](images\4_21.png)


### 4.22. Representing Graphs

``` sql
sqllllll
```
![pic](images\4_22.png)


### 4.23. Recursive Queries

``` sql
sqllllll
```
![pic](images\4_23.png)


### 4.24. Bidirectional Contacts

``` sql
sqllllll
```
![pic](images\4_24.png)


### 4.25. Updating Group Identifiers

``` sql
sqllllll
```
![pic](images\4_25.png)


### 4.26. Recursive Labeling

``` sql
sqllllll
```
![pic](images\4_26.png)


### 5.1. Querying from Python

``` python
pythonnnn
```
![pic](images\5_1.png)


### 5.2. Incremental Fetch

``` python
pythonnnn
```
![pic](images\5_2.png)


### 5.3. Insert, Delete, and All That

``` python
pythonnnn
```
![pic](images\5_3.png)


### 5.4. Interpolating Values

``` python
pythonnnn
```
![pic](images\5_4.png)


### 5.5. Script Execution

``` python
pythonnnn
```
![pic](images\5_5.png)


### 5.6. SQLite Exceptions in Python

``` python
pythonnnn
```
![pic](images\5_6.png)


### 5.7. Python in SQLite

``` python
pythonnnn
```
![pic](images\5_7.png)


### 5.8. Handling Dates and Times

``` python
pythonnnn
```
![pic](images\5_8.png)


### 5.9. Pandas and SQL

``` python
pythonnnn
```
![pic](images\5_9.png)


### 5.10. Polars and SQL

``` python
pythonnnn
```
![pic](images\5_10.png)


### 5.11. Object-Relational Mappers

``` python
pythonnnn
```
![pic](images\5_11.png)


### 5.12. Relations with ORMs

``` python
pythonnnn
```
![pic](images\5_12.png)

### THATS ALL FOLKS