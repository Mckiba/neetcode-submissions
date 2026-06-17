class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        len_seq = ",".join(str(len(word)) for word in strs)
        raw = "".join(strs)
        return len_seq + "#seq?" + raw

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        seq_str, org_str = s.split("#seq?", 1)
        codes = seq_str.split(',') if seq_str else []
        words = []
        i = 0
        for index in codes:
            num = int(index)
            words.append(org_str[i:i+num])
            i += num
        return words
