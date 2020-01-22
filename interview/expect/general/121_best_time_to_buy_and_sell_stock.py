"""
121. Best Time to Buy and Sell Stock
Easy

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0

        min_idx = profit = 0
        max_idx = 1
        while max_idx <= len(prices) - 1:
            #if meet smaller one just swap min idx to that because everything before that lose their meanining to exist.
            #1. You don't need to do anything with it. 2 smaller can make more profit than bigger one.
            if prices[max_idx] < prices[min_idx]:
                min_idx = max_idx
                max_idx = min_idx + 1
            else:
                #it can keep going ahead as the smallest one.
                new_profit = prices[max_idx] - prices[min_idx]
                if new_profit > profit:
                    profit = new_profit
                max_idx += 1
        return profit


    # 매번 순서에서 현재순서-앞의순서 한것을 loc에 더한것을 비교하는 것은 어차피 큰수는 global에 들어가있으므로, 여기서 loc이 이전의 loc보다 작아지는 것은 신경쓸 필요가 없다.
    # 어차피 완전히 마이너스로 내려가는게 아닌이상 이전의 축적이 있는것에 더해나가는 것이 더 큰수를 만드는 경우이므로 계속 더해나가 보는게 맞는 것이고,
    # 그 과정에서 이전보다 조금 줄더라도 이미 큰 수는 glo에 가장 큰 수로서 한번 저장을 하고 있기때문에 신경쓸 것 없이 계속 나아가면 된다.
    # 어쨌든 이전의 축적 loc을 아예 -로 만드는 경우는 끊어버리고 다시가는게 맞는거고,
    # 그렇지 않으면 축적해 나가는게 더 큰 수의 가능성으로 가는 것이다.
    # 어차피 그곳의 두수의 차가 양수라면 거기서 시작하는 수도 양수고, 축적된 것에 더하는 것도 양수이므로 축적을 통해 다음으로 계속 향해보는게 맞다.
    # 그렇게 glo를 쌓아가다가 glo를 return
    def maxProfit1(self, prices):
        if not prices:
            return 0
        loc = glo = 0
        for i in range(1, len(prices)):
            loc = max(loc + prices[i] - prices[i - 1], 0)
            print(loc, prices[i], prices[i-1])
            glo = max(glo, loc)
        return glo

s = Solution()
p = [7,1,5,3,6,4]
p = [2,10,1,3,4,25]
print(s.maxProfit(p))