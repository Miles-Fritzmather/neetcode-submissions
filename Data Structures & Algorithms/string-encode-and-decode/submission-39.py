class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        while (len(s) != 0):
            cut = s.split("#", 1)
            num = int(cut[0])
            res.append(cut[1][0:num])
            s = cut[1][num:]
        return res
        