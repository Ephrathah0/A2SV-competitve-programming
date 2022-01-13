class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        if len(tokens) == 1: 
            return int(tokens[0])
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                sec = stack.pop()
                fir = stack.pop()
                temp=0
                if token == '+':
                    temp = fir + sec
                elif token == '-':
                    temp = fir - sec
                elif token == '*':
                    temp = fir * sec
                elif token == '/':
                    temp = fir / sec
                    temp = math.trunc(temp)
                stack.append(temp)
        return stack.pop()