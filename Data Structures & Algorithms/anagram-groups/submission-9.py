class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        s_dict = {}
        for string in strs:
            s = "".join(sorted(string))
            if s in s_dict:
                s_dict[s].append(string)
            else:
                s_dict[s] = [string]
        return (list(s_dict.values()))