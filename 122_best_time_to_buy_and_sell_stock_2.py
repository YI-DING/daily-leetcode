from math import inf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        in_hand,summ=inf,0
        length=len(prices)
        for i in range(length):
            if in_hand is inf:#no stocks in hand
                if i<length-1:#not the last day
                    if prices[i]<prices[i+1]:
                        in_hand=prices[i]#buy in 
                        summ-=prices[i]
            else:#stocks in hand
                if i==length-1:#last day
                    summ+=prices[i]
                else:
                    if prices[i]>prices[i+1]:#sell
                        summ+=prices[i]
                        in_hand=inf
        return (summ)
#return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
#note this simplest solution does not conceptually align with 'no buying selling at same day'.