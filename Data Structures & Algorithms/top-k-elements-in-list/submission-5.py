class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        # create an map with the number of occurences as the key and the 
        #numbers that appeat that many times as the key


        #1.   2.  3.  4.  5.  6.
        #[1] [2] [3] [4] [5]

        freq = {}
        heap = [ [] for i in range(len(nums) + 1)  ]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        print(heap)
        for item, val in freq.items():
            print(item, val)
            heap[val].append(item)

        l = []
        for i in range(len(heap) - 1, 0, -1):
            for num in heap[i]:
                if len(l) < k:
                    l.append(num)
                else:
                    break
                

        return l


        