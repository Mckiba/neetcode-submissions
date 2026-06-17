class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        #sort first str
        #check all string agaist sorted versions
        #if sorted are equal add it to the key of sorted version 

        groups = {}

        for word in strs:
            st =  "".join(sorted(word))
            if st in groups:
                groups[st].append(word)
            else:
                groups[st] = [word]
        
        return list(groups.values())

