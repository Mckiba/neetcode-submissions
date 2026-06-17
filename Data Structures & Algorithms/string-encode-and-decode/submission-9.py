class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        len_seq = [str(len(word)) for word in strs ]    
        return "".join(strs) + "#seq?" + ",".join(len_seq)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        org_str = s.split("#seq?")[0]
        codes = s.split("#seq?")[-1].split(',')
        words = []
        for index in codes:
            num = int(index)
            words.append(org_str[:num])
            org_str = org_str[num:]
        return words
