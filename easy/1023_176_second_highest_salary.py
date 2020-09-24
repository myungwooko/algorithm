"""
176. Second Highest Salary
Easy

582

311

Favorite

Share
SQL Schema
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+


select * from employee order by salary desc limit 1,1
Description : limit x,y
x: The row offset from which you want to start displaying records. For nth record it will be n-1.
y: The number of records you want to display. (Always 1 in this case)


select salary from table order by salary desc limit 0,1
// for highest salary of table
select salary from table order by salary desc limit 1,1
// for second highest salary

*******
query *
*******

- LIMIT A B
A = {시작지점index느낌(0부터유효)}
B = {시작지점부터개수(1부터count)}

- IFNULL
SELECT TaskCode
From Tasks;
Result:

+----------+
| TaskCode |
+----------+
| gar123   |
| NULL     |
| NULL     |
| dog456   |
| NULL     |
| cat789   |
+----------+
So we have three NULL values and three non-NULL values.

The IFNULL() Function
Given its name, this is probably the most obvious option for replacing NULL values in MySQL. This function is basically the equivalent of ISNULL() in SQL Server.

The IFNULL() function allows you to provide two arguments. The first argument is returned only if it is not NULL. If it is NULL, then the second argument is returned instead.

Here’s an example of using IFNULL() against our sample data set:

SELECT IFNULL(TaskCode, 'N/A') AS Result
FROM Tasks;
Result:

+--------+
| Result |
+--------+
| gar123 |
| N/A    |
| N/A    |
| dog456 |
| N/A    |
| cat789 |
+--------+
"""
"""
아래의 input에 대해서 
#1 query는 [] => value가 아예 없음으로 리턴하고,
#2 query는 [null] => value null(값이 없음)으로 결과를 리턴한다. 
 
input {"headers": {"Employee": ["Id", "Salary"]}, "rows": {"Employee": [[1, 100]]}}
"""
#1
"""
select Salary as SecondHighestSalary from Employee order by Salary desc limit 1,1
"""
#=> {"headers": ["SecondHighestSalary"], "values": [[]]}

#2
"""
Select MAX(Salary) as SecondHighestSalary from Employee where Salary < (Select MAX(Salary) from Employee)
"""
#=> {"headers": ["SecondHighestSalary"], "values": [[null]]}
