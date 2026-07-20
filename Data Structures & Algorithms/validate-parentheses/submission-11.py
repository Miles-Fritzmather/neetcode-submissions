class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{": stack.append(c)
            if matches.get(c) is not None and (len(stack) == 0 or stack.pop() != matches[c]): return False
        
        return len(stack) == 0
            