class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c.lower() for c in s if c.isalnum()])
        print(s)
        for i in range(0, len(s) // 2):
            print(i, s[i], s[-i])
            if s[i] != s[-1 -i]: return False
        return True
        