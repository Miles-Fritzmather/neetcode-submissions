class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{": stack.append(c)

            if c == ")" and (len(stack) == 0 or (len(stack) != 0 and stack.pop() != "(")):  return False
            if c == "}" and (len(stack) == 0 or (len(stack) != 0 and stack.pop() != "{")):  return False
            if c == "]" and (len(stack) == 0 or (len(stack) != 0 and stack.pop() != "[")):  return False
        
        return len(stack) == 0
            