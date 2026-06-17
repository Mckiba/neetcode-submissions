from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n_dict = dict(Counter(nums))

        sorted_dict = list(key[0] for key in sorted(n_dict.items(), key=lambda item:item[1], reverse=True))[:k]
      
        return sorted_dict
        
        