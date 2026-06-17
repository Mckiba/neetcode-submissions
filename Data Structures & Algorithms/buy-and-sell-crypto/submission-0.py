class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        index = 0
        best = 0

        while index < len(prices) - 1:
            n = prices[index]
            print(index)
            window = prices[index+1:]
            print('N',n)
            largest = max(window)
            print(window, largest)
            best = max(largest - n, best)
            print('best', best)
            index += 1


        
        
        return best
