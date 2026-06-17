class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count  = {}
        res = 0

        l = 0
        r = 0

        while r < len(s):
            window = s[l:r+1]
            print("WINDOW",window)
            counts = Counter(window)
            print(counts)

            # check the maximum element
            # replacement needed is size - max 
            max_element = max(counts.values())
            print(max_element)
            print("LEN",len(window))
            dif = (len(window) - max_element)
            print("DIF", dif)
            if k >= dif:
                print('valid window', window)
                # increase size of window
                r+=1
            else:
                l+=1
                continue
            res = max(res, len(window))
        print(res)
        return res
                    
        