class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        index,best = 0,0

        while index < len(prices) - 1:
            n = prices[index]
            window = prices[index+1:]
            largest = max(window)
            best = max(largest - n, best)
            index += 1
        return best
