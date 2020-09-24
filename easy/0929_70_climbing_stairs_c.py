"""
7
[1, 1, 1, 1, 1, 1, 1]
[2, 1, 1, 1, 1, 1] = > 1
[1, 2, 1, 1, 1, 1] = > 2
[1, 1, 2, 1, 1, 1] = > 3
[1, 1, 1, 2, 1, 1] = > 4
[1, 1, 1, 1, 2, 1] = > 5
[1, 1, 1, 1, 1, 2] = > 6

[2, 2, 1, 1, 1]
[2, 1, 2, 1, 1]
[2, 1, 1, 2, 1]
[2, 1, 1, 1, 2]
[1, 2, 2, 1, 1]
[1, 2, 1, 2, 1]
[1, 2, 1, 1, 2]
[1, 1, 2, 2, 1]
[1, 1, 2, 1, 2]
[1, 1, 1, 2, 2]

[2, 2, 2, 1]
[2, 2, 1, 2]
[1, 2, 2, 2]


4
[1,1,1,1]
[2,1,1]
[1,2,1]
[1,1,2]
[2,2]



[1,1,1,1] => cont = 1
recursion([1.1.1.1])
=> [[1,1,1], [1,1], [1]]



********************
개념은 결국 최종목적지에서 왼쪽이 계단 두개내려간거고 오른쪽이 하나 내려간걸 나타낸다면 결국 왼쪽에서 한칸 올라오는 선택하면 도착하고, 오른쪽에서 두칸 올라오면 도착하는게 되니까
결국 두칸 아래까지 올라오는 방법 + 한칸 아래까지 올라오는 방법 두개의 개수를 더하면 해당 목적지 까지 다다르는 방법의 개수가 된다. 한번에 올라갈수 있는 칸의 개수는 1 or 2인데 그 지점들에서 올라오는건 그 방법밖에 없고 그게 끝이므로.
(아래 숫자는 계단의 칸 위치를 나타낸)


            7
          /  \
        5     6
       / \   / \
      3   4 4   5

      이런식으로 생각하면 된다.


"""


class Solution:
    def __init__(self):
        self.count = 0

    def climbStairs(self, n: int) -> int:
        # q = max number how many 2 exist in the combination
        # for combination max 2, whether 1 can exist or not
        # recursion
        # 넣으면 1짝을 2로 만들수 있는애들 각각 만들고 count 만든애를 recursion
        # recursion은 들어오면 2 뒤의 1들을 2로 만드는 짝
        """
        이걸로 답은 같게 나오는것 같은데 시간이 너무 오래 걸린다.
        """

        if n <= 1:
            return n
        self.count += 1  # add first[1,1,1,1,1]
        ones = [1] * (n)

        self.recursion(ones)
        return self.count

    def recursion(self, li):
        # [1,1,1,1,1]
        if len(li) <= 1:
            return
        self.count += len(li) - 1
        default = [1] * (len(li) - 1)
        # [1,1,1,1]
        res = []
        for i, v in enumerate(default):
            ele = default[:][i + 1:]
            res.append(ele)

        for ele in res:
            self.recursion(ele)

    def climbStairs1(self, n):
        """
        # recursion
        이것도 오래걸리지만 그나마 내가 한것 보단 나은거 같다. Time complexity O(2**n) => 층위는 그만큼이고(=n) 층위마다 항상 2개의 계산을 하니까 2**n
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs1(n - 1) + self.climbStairs1(n - 2)

    def climbStairs2(self, n):
        """
        # Bottom up, memoization => Time complexity O(n) space O(n)
        뤟씬 빠르다. 했던 계산까지 막 다해보는게 아니니까
        이런식의 경우 처음 두값만 알면 오케이고 효율성 좋음.
        """
        if n == 1:
            return 1
        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]
        return res[-1]


s = Solution()
test1 = s.climbStairs(35)
print(test1)
test2 = s.climbStairs1(35)
print(test2)
test3 = s.climbStairs2(35)
print(test3)
