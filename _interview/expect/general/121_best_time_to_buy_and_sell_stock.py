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



    def maxProfit(self, prices):
        if not prices:
            return 0
        loc = glo = 0
        for i in range(1, len(prices)):
            # 이게 아예 그 값을 구하는 식이네 => 1, 5, 3 이 있으면 5-1 이랑 3-5 를 더하면 3-1이 된다.
            # 그러므로 (loc + prices[i] - prices[i - 1]) 해당 식은 => (prices[i] - 현재 집고 있는 것)을 의미한다.
            # 근데 이 값이 -가 나왔다는건 prices[i]가 현재 집고 있는것 보다 싼것이라는 의미이므로 다음에 만나는 수들에 대해서는 그것(prices[i])를 집고 시도해보는게
            # 더 이익을 낼수 있는 가능성에 대한 탐색이라는 얘기가 된다.
            # 그리고 그 다음의 탐색에서 최대값을 찾지 못해도 문제는 없다.(예를 들어 계속 더 놓은 값이 안나온다든지)
            # 우리는 이미 glo를 통해 최대값을 갖고 있기 때문에.
            loc = max(loc + prices[i] - prices[i - 1], 0)
            # print(loc, prices[i], prices[i-1])
            glo = max(glo, loc)
        return glo

s = Solution()
p = [7,1,5,3,6,4]
p = [2,10,1,3,4,25]
print(s.maxProfit(p))