class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        len_seq = []
        for word in strs:
            len_seq.append(str(len(word)))
        enc_str = "".join(strs) + "#seq?" + ",".join(len_seq)
        return enc_str

    def decode(self, s: str) -> List[str]:
        print(s)
        if not s:
            return []
        seq = s.split("#seq?")[-1]
        org_str = s.split("#seq?")[0]
        codes = seq.split(',')
        words = []
        for index in codes:
            print(words)
            print(codes)
            num = int(index)
            words.append(org_str[:num])
            org_str = org_str[num:]

        return words
