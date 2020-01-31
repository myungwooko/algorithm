class Solution:
    # BFS => => Time Limit Exeeded
    def coinChange(self, coins, amount):
        coins.sort()
        if amount == 0 and coins[0] > amount:
            return 0
        idx = len(coins) - 1
        count = 0
        queue = [(count, amount, idx)]
        while queue:
            count, amount, idx = queue.pop(0)
            if idx == -1:
                if amount == 0:
                    return count
                continue
            divider = coins[idx]
            q, r = divmod(amount, divider)
            for i in range(q, -1, -1):
                if idx >= 0:
                    queue.append((count + i, amount - (divider * i), idx - 1))
        return -1

    # #DFS => => Time Limit Exeeded
    def coinChange(self, coins, amount):
        coins.sort()
        counts = []

        def helper(amount, idx, count):
            if amount == 0:
                counts.append(count)
                return
            dvider = coins[idx]
            q = amount // dvider
            for i in range(q, -1, -1):
                diff = coins[idx] * i
                # idx가 0인 것까지는 해줘야지 그래야 그것까지를 계산해준게 되니까
                if idx >= 0:
                    helper(amount - diff, idx - 1, count + i)

        helper(amount, len(coins) - 1, 0)
        if counts:
            return min(counts)
        return -1

    """
    Classic case of dynamic programing and counter example of greedy.
    dp[i] records the minimal coins needed to make up amount i. And it's one more coin than the minimum of dp[i-j] for j in coins.
    All value in dp array are initialized as None. If all possibile dp[i-j] are None, amount i is not reachable by any combination of coins 
    as we leave it as None as well. And I set a None value as -1 since we are required to return -1 if i is not able to be made up of.

    - dp[i-c]의 의미:
   *- dp에서 해당 index는 그 index만큼의 amount를 지칭
    - 그러므로 index => i - c(코인중 하나의 값) 의 의미는 amount i - amount c 인 amount가 되고
    - 현재의 dp의 값은 해당 index이자 amount에 대한 coin의 최소개수를 나타내고 있으므로
    - dp[i-c] => i에서 코인값 중 하나인 c를 뺀 amount에 대한 최소 coin의 개수를 나타냄.
    - 여기에 방금 뺐던 코인에 대한 개수 1을 더해주면 dp[i] 즉 amount i에 대한 최소코인의 개수 값을 구하게 된다. 
    - 이게 가능한 이유는 작게 쪼개진 앞의 부분 amount에 대한 값에 대해 최소개수를 dp에 차곡차곡 쌓아 나갔기 때문.
    - 여기서 없으면 amount를 넘는 max로 표시해놓고, 가능한건 구해놓으면서 
    - 결국 그걸 가져다가 조회하고 만들어봄으로 가능한지를 가늠하고, 실제 그 개수 또한 구하게 된다.
    - 그러므로 해당 index보다 작은 것들은 모두 값이 구해져있으니 그렇게 조회해보고 그중에 가장 작은걸 선택
    - 해당 coin 값 하나를 빼서 구한거니깐 당연히 더해준다. 
    - 굉장히 smart하게 index자체가 i와 mapping 되게 한 것.
      이해!!!
    """
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = amount + 1
        dp = [MAX] * (MAX)
        # 0을 만드는데는 무조건 코인 0개가 필요하니깐.
        dp[0] = 0
        for i in range(1, MAX):
            dp[i] = min([dp[i - c] if i >= c else (MAX) for c in coins])  ### List Comprehension is faster
            # 그렇게 유효한 값이 구해진 경우에만 개수 + 1을 해준다. 그렇지 않은 경우 값이 구해지지 않은 의미로서 MAX를 그대로. 그래야 일관성이 생겨서 참고 가능.
            dp[i] = dp[i] + 1 if dp[i] != MAX else dp[i]
        return -1 if (dp[-1] == MAX) else dp[-1]

    #same cleaner
    def coinChange(self, coins, amount):
        MAX = amount + 1
        dp = [MAX] * MAX
        dp[0] = 0
        for i in range(1, MAX):
            dp[i] = min(dp[i - coin] if i >= coin else MAX for coin in coins)
            dp[i] = dp[i] + 1 if dp[i] != MAX else MAX
        return dp[-1] if dp[-1] != MAX else -1