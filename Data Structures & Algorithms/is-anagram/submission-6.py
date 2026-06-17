class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1, word2 = {}, {}

        if len(word2) != len(word1):
            return False

        for char in s:
            word1[char] = word1.get(char, 0) + 1
        for char in t:
            word2[char] = word2.get(char, 0) + 1

        return word1 == word2 