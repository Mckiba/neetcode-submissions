class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = []
        found = set()

        
        def getFreq(string: str) -> dict:
            dict1 = {}
            for char in string:
                if char in dict1:
                    dict1[char] = dict1[char] + 1
                else:
                    dict1[char] = 1
            return dict1
            

        def isAnagramOf(string: str, an_dict: dict):
            new_dict = {}
          
            for char in string:
                if char in new_dict:
                    new_dict[char] = new_dict[char] + 1
                else:
                    new_dict[char] = 1

            print("ASAS", an_dict)
            print(new_dict)
            
            for char, count in new_dict.items():
                if an_dict.get(char, 0) != count:
                    return False
            return True


        for index, word in enumerate(strs):
            sub_list = [word]
            print("AT WORD", word)
            my_dict = getFreq(word)
            print(my_dict)
            if word not in found:
                for string in strs[index+1:]:
                    print(f"CHECKING, {word}, AGAINST, {string}")
                    if len(string) == len(word) and isAnagramOf(string, my_dict):
                        print("IS AN ANAGRAM")
                        found.add(string)
                        sub_list.append(string)
                anagrams.append(sub_list)


             

            

            


        return anagrams
        





# for index, string in enumerate(strs):
#             anagram_subs=[]
#             dict1 = getFreq(string)
#             # print("dict1", dict1)
#             # print(string, index)
            
#             #loop thorugh all other string and check for anagrams
#             for i in range(index+1):
#                 if isAnagramOf(string, dict1):
#                     anagram_subs.append(string)
                
            
            
#             print(anagrams.append(anagram_subs))
 


#         print(anagrams)


