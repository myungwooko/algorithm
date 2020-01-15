"""
937. Reorder Data in Log Files
Easy

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier,
with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.



Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]


Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""
class Solution:
    def reorderLogFiles(self, logs):
        # letter should be before digit
        # let => lexiograpically order
        # dig => 원래 order
        dic = {}
        for i in range(len(logs)):
            splitted = logs[i].split(" ")
            if not splitted[1].isnumeric():
                if " ".join(splitted[1:]) not in dic:
                    dic[" ".join(splitted[1:])] = [splitted[0]]
                else:
                    dic[" ".join(splitted[1:])].append(splitted[0])
                    dic[" ".join(splitted[1:])] = sorted(dic[" ".join(splitted[1:])])
        dig = [i for i in logs if i.split(" ")[1].isnumeric()]
        let = [" ".join(i.split(" ")[1:]) for i in logs if not i.split(" ")[1].isnumeric()]
        let.sort()
        let = [dic[i].pop(0) + " " + i for i in let]
        res = let + dig
        return res

    def reorderLogFiles(self, logs):
        def f(log):
            id, rest = log.split(" ", 1)
            # letter 인 경우 일단 dig보다 앞으로 오고 그 안에서 rest를 비교하고 그 다음 id를 비교하겠다는 의미
            # 여기서 dig같은 경우 그냥 (1, ) 보냈는데 뒤의 내용은 비교하지 않겠다는 의미이고 letter 보다는 뒤니까 그것만 해주는 의미.
            return (0, rest, id) if rest[0].isalpha() else (1,)
        return sorted(logs, key=f)
