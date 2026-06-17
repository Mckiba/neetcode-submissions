class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        freq = {}
        l = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        freq_sorted = sorted(freq.items(), key = lambda x:x[1], reverse=True)
        print(freq_sorted)
        for i in range(k):
            l.append(freq_sorted[i][0])
        return l 


        