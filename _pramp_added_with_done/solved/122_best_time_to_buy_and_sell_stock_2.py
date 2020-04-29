"""
122. Best Time to Buy and Sell Stock II
Easy

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is _pramp_added_with_done, i.e. max profit = 0.
Accepted

-처음의 문제 파악이 정말 중요하다.
0. 같은 날 사고 파는 건 불가하다.
- 들고있지않을때 if: a1-a0 > a2- a1 이면 a0은 산다.
             else: to_buy_index += 1, to_sell_index += 1
- 들고있을때 => if: a[sell_index] - a[buy_index] > 0 이고,
                if:   a[sell_index+1] - a[sell_index] < 0 판다. => index는 sell_index + 1 에서 사는 논리 시작.
                else: a[sell_index+1] - a[sell_index] >= 0 이면 팔지 않고 sell_index += 1,
=> 위는 조건 0부터 잘못되었었다.

=> 문제 파악이 정말 중요하다... 같은날 팔고나서 사는건 가능한 거였다...............
"""
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        return sum([max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1)])
