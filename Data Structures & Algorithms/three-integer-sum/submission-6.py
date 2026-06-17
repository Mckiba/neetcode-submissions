class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
 


        n = sorted(nums)

        vals = []
        print(n)


        for index,num in enumerate(n):

           
             
            l = index + 1
            r = len(n)-1

            print(l, r)
        

        
            while l < r:
                lval = n[l]
                rval = n[r]

                sum = lval + rval
              

                if sum == (num * -1):
                    if [num, lval, rval] not in vals:
                        vals.append([num, lval, rval])
                    l+1
                    r-=1
                elif sum < (num * -1):
                    l += 1
                else:
                    r -= 1
        return vals
            
        
        

