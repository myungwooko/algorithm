"""
1179. Reformat Department Table

SQL Schema
Table: Department

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| revenue       | int     |
| month         | varchar |
+---------------+---------+
(id, month) is the primary key of this table.
The table has information about the revenue of each department per month.
The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].


Write an SQL query to reformat the table such that there is a department id column and a revenue column for each month.

The query result format is in the following example:

Department table:
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+

Result table:
+------+-------------+-------------+-------------+-----+-------------+
| id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1    | 8000        | 7000        | 6000        | ... | null        |
| 2    | 9000        | null        | null        | ... | null        |
| 3    | null        | 10000       | null        | ... | null        |
+------+-------------+-------------+-------------+-----+-------------+

Note that the result table has 13 columns (1 for the department id + 12 for the months).
"""

"""
SELECT id,
MAX(CASE WHEN month='Jan' then revenue else null end) as Jan_Revenue,
MAX(CASE WHEN month='Feb' then revenue else null end) as Feb_Revenue,
MAX(CASE WHEN month='Mar' then revenue else null end) as Mar_Revenue,
MAX(CASE WHEN month='Apr' then revenue else null end) as Apr_Revenue,
MAX(CASE WHEN month='May' then revenue else null end) as May_Revenue,
MAX(CASE WHEN month='Jun' then revenue else null end) as Jun_Revenue,
MAX(CASE WHEN month='Jul' then revenue else null end) as Jul_Revenue,
MAX(CASE WHEN month='Aug' then revenue else null end) as Aug_Revenue,
MAX(CASE WHEN month='Sep' then revenue else null end) as Sep_Revenue,
MAX(CASE WHEN month='Oct' then revenue else null end) as Oct_Revenue,
MAX(CASE WHEN month='Nov' then revenue else null end) as Nov_Revenue,
MAX(CASE WHEN month='Dec' then revenue else null end) as Dec_Revenue
From
Department
Group By id
-(as 없어도 된다) 
SELECT id,
MAX(CASE WHEN month='Jan' then revenue else null end) Jan_Revenue,
MAX(CASE WHEN month='Feb' then revenue else null end) Feb_Revenue,
MAX(CASE WHEN month='Mar' then revenue else null end) Mar_Revenue,
MAX(CASE WHEN month='Apr' then revenue else null end) Apr_Revenue,
MAX(CASE WHEN month='May' then revenue else null end) May_Revenue,
MAX(CASE WHEN month='Jun' then revenue else null end) Jun_Revenue,
MAX(CASE WHEN month='Jul' then revenue else null end) Jul_Revenue,
MAX(CASE WHEN month='Aug' then revenue else null end) Aug_Revenue,
MAX(CASE WHEN month='Sep' then revenue else null end) Sep_Revenue,
MAX(CASE WHEN month='Oct' then revenue else null end) Oct_Revenue,
MAX(CASE WHEN month='Nov' then revenue else null end) Nov_Revenue,
MAX(CASE WHEN month='Dec' then revenue else null end) Dec_Revenue
From
Department
Group By id
"""

# Process + a
# id로 GROUP BY 한다.
# 각각의 id에서 CASE가 해당 달이면 그건 revene를 가져오고 나머지는 null로 채운다.
# 그것에서 MAX를 뽑는다
# 그것을 해당달_Revenue column에 넣는다.
# 그것은 모든 달에 대해서 하는 개념.
# + then else end 는 일단 소문자로

# """
# 아래를 보면 +GROUP BY에 대한 이해가 됨.
# Q:Why MAX?
#
# A: In the 'Department' table -> Each 'id' has 12 rows across 'month'.
# Hence, the 'Case' statement for each 'id' will return 12 values - eleven 'null' values + revenue for the month specified in the 'WHEN' clause.
# Since we do not require all twelve values, and are only interested in the revenue that was returned for the particular month, we take 'MAX'
# since it will always return the revenue as the remaining eleven values are NULL.
# """
