class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        c =  Counter(nums).most_common(k)
        freq = []

        for nums in c:
            freq.append(nums[0])
        return freq
        