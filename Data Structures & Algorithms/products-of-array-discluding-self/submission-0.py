class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        #[1,2,4,6] = 6 * 1 * 3 * 4
        #__________________
        #(0,1) [2,4,6] = 48
        #(1,2) [1,4,6] = 24
        #(2,4) [1,2,6] = 12
        #(3,6) [1,2,4] = 8

        res = []

        
        for i in range(len(nums)):
            l = 0
            r = len(nums) - 1 
            prod = []
            while l < i or r > i:
                if l < i:
                    prod.append(nums[l])
                    l+=1
                if r > i:
                    prod.append(nums[r])
                    r-=1
            res.append(math.prod(prod))


            

            
        
        return res

        
        


    




        # two pointers at the end of that number
        #multiple until you get to that number?
        #l = end of list
        #r = index 0 or index + 1 if num is at 0
        #l = 2, r  = 6
        #2 * 6
        #


