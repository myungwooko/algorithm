"""
178. Rank Scores
Medium

674

109

Add to List

Share
SQL Schema
Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie,
the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.

+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
For example, given the above Scores table, your query should generate the following report (order by highest score):

+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
"""
"""
SELECT Score, (SELECT COUNT(DISTINCT t2.Score)+1 FROM Scores AS t2
              WHERE t1.Score < t2.Score) AS Rank
FROM Scores AS t1
ORDER BY Score DESC
"""



# 내용: t2가 t1의 score보다 큰것은 distinct하게 구분해서(Score기준) count를 하는데 기본 0부터 시작이니까 +1해주는 것으로 해서 Rank로서 넣어준다.

# plus concept
# 간단하게 as로 넣어줄수 있다.
# table 자체를 바꾸는 것(ALTER)은 권한이 필요하다.
# as는 바로 뒤에 붙여주면 적용된다. (생략해도 보통 적용된다.)