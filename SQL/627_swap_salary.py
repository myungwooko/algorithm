"""
627. Swap Salary
Easy

409

272

Add to List

Share
SQL Schema
Given a table salary, such as the one below, that has m=male and f=female values. Swap all f and m values
(i.e., change all f values to m and vice versa) with a single update statement and no intermediate temp table.

Note that you must write a single update statement, DO NOT write any select statement for this problem.



Example:

| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
After running your update statement, the above salary table should have the following rows:
| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |
"""
# Write your MySQL query statement below
"""
UPDATE salary
SET sex = CASE sex WHEN 'm' THEN 'f' 
                   WHEN 'f' THEN 'm'
                   END
                   WHERE sex IN ('m', 'f');
"""

# You want to use a CASE expression of some type.
# In SQL Server the code would look like this:
"""
UPDATE TableName
SET gender = CASE WHEN gender = 'M' THEN 'W' 
                  WHEN gender = 'W' THEN 'M'
                  ELSE gender END
"""

# Edit: As stated in the comments (and some of the other answers) the ELSE isn't necessary if you put a WHERE clause on the statement.
"""
UPDATE TableName
SET gender = CASE WHEN gender = 'M' THEN 'W' 
                  WHEN gender = 'W' THEN 'M' END
WHERE gender IN ('M','W')
"""

# This avoids unnecessary updates. The important thing in either case is to remember that there are options other than M & W (NULL for example) and you don't want to put in mistaken information. For example:
"""
UPDATE TableName
SET gender = CASE WHEN gender = 'M' THEN 'W' 
                  ELSE 'M' END
"""

# This would replace any NULLs (or other possible genders) as 'M' which would be incorrect.

# A couple of other options would be

# Simple form of CASE rather than Searched form*/
"""
UPDATE TableName
SET    gender = CASE gender
                WHEN 'M' THEN 'W'
                WHEN 'W' THEN 'M'
                END
WHERE  gender IN ( 'M', 'W' );

"""
