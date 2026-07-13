class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)

            right = dfs()
            left = dfs()

            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            elif token == '/':
                return int(left / right)

        def stack():
            my_stack = []

            for token in tokens:
                if token not in '+-*/':
                    my_stack.append(int(token))
                else:
                    right = my_stack.pop()
                    left = my_stack.pop()
                    res = 0
                    if token == '+':
                        res = left + right
                    elif token == '-':
                        res = left - right
                    elif token == '*':
                        res = left * right
                    elif token == '/':
                        res = int(left / right)
                    my_stack.append(res)
            return my_stack.pop()


        return stack()