class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False

        s_dict = {}
        t_dict = {}

        for c in t:
            if c in t_dict:
                t_dict[c] = t_dict[c]+1
            else:
                t_dict[c] = 1

        for c in s:
            if c in s_dict:
                s_dict[c] = s_dict[c]+1
            else:
                s_dict[c] = 1
             
        for char in s_dict:
            if char not in t_dict:
                return False
            if t_dict[char] != s_dict[char]:
                return False

        return True