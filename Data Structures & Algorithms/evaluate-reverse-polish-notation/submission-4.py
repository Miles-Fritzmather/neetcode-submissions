class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for token in tokens:
            print(numbers, token)
            if token == "+":
                a = numbers.pop()
                b = numbers.pop()
                numbers.append(int(a+b))
            elif token == "-":
                a = numbers.pop()
                b = numbers.pop()
                numbers.append(int(b-a))
            elif token == "/":
                a = numbers.pop()
                b = numbers.pop()
                numbers.append(int(b / a))
            elif token == "*":
                a = numbers.pop()
                b = numbers.pop()
                numbers.append(int(a*b))
            else: 
                numbers.append(int(token))
        return int(numbers.pop())
            