class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        operators = {
            "+": lambda a, b: b + a,
            "-": lambda a, b: b - a,
            "*": lambda a, b: b * a,
            "/": lambda a, b: b / a,
        }
        for token in tokens:
            if (val := operators.get(token)) is not None:
                numbers.append(int(val(numbers.pop(), numbers.pop())))
            # if token == "+":
            #     a = numbers.pop()
            #     b = numbers.pop()
            #     numbers.append(int(a+b))
            # elif token == "-":
            #     a = numbers.pop()
            #     b = numbers.pop()
            #     numbers.append(int(b-a))
            # elif token == "/":
            #     a = numbers.pop()
            #     b = numbers.pop()
            #     numbers.append(int(b / a))
            # elif token == "*":
            #     a = numbers.pop()
            #     b = numbers.pop()
            #     numbers.append(int(a*b))
            else: 
                numbers.append(int(token))
        return int(numbers.pop())
            