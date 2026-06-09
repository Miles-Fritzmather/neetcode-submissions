class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        if s == "": return []

        res = []
        while (len(s) != 0):
            # print("s: ", s, len(s))
            cut = s.split("#", 1)
            num = int(cut[0])
            res.append(cut[1][0:num])
            # print("cut: ", cut)
            # print("new element: ", cut[1][0:num])
            # print("current return: ", res)
            s = cut[1][num:]
            # print("rest: ", s, len(s))
        return res
        