class Solution:
    def maxArea(self, heights: List[int]) -> int:


        l = 0
        r = len(heights)-1

        cap = ((len(heights)-1) - 0) * (min(heights[0], heights[len(heights)-1]))
        print(cap) 

       




        #find a greater cap  
        while l < r:


            lval = heights[l]
            rval = heights[r]

            print(l, lval)
            print(r, rval)

            sum = (r - l) * (min(lval, rval))
            if sum > cap:
                cap = sum 

            if lval < rval:
                l += 1
            elif rval < lval:
                r -= 1
            else:
                l += 1

            print(cap)

        return cap

            

        # (0,1) index, val
        # (7,6) index, val




        # move the smaller stick
        # (1,2) index, val
        # (7,6) index, val

        # 7 - 1 * 2
        # cap = 12
        # loop ends and cap is 12



        
        # cap = space between them times min quant

        # find the next two largest cap 
        # starting at index and end 

        # (7,2)
        # (6,7)

        # sum = (r(index) - l(index)) * (min(lval, rightval)) 

        

        # if sum < cap



        




    