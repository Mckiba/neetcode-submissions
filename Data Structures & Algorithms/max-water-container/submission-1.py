class Solution:
    def maxArea(self, heights: List[int]) -> int:


        l, r = 0, len(heights)-1
        cap = (r - l) * (min(heights[l], heights[r]))

        while l < r:
            lval = heights[l]
            rval = heights[r]

            sum = (r - l) * (min(lval, rval)) 
            if sum > cap:
                cap = sum 

            if lval < rval:
                l += 1
            elif rval < lval:
                r -= 1
            else:
                l += 1

        return cap