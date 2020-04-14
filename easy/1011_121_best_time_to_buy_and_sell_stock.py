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
Explanation: In this case, no transaction is done_with_pramp, i.e. max profit = 0.
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

    #하나하나 축적하고 비교해나가면서 => 해당 순서와 축적된 것의 비교에서 그럼에도 양수라는 것은 최소로서 갖고 있는 현재의 것이 여전히 최소라는 의미이다.
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