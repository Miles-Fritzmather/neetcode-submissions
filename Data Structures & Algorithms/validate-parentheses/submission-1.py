class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(": stack.append("(")
            if c == ")": 
                if len(stack) == 0: return False
                val = stack.pop()
                if val != "(": return False

            if c == "{": stack.append("{")
            if c == "}": 
                if len(stack) == 0: return False
                val = stack.pop()
                if val != "{": return False

            if c == "[": stack.append("[")
            if c == "]": 
                if len(stack) == 0: return False
                val = stack.pop()
                if val != "[": return False
        
        return len(stack) == 0
            