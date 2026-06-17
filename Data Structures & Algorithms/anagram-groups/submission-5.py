class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = {}
        for word in strs:
            w = "".join(sorted(word))
            if w in new_dict:
                new_dict[w].append(word)
            else:
                new_dict[w] = [word]
        return list(new_dict.values())
        
