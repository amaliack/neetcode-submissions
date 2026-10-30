class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                operand_two = stack.pop()
                operand_one = stack.pop()
                res = None
                if t == "+":
                    res = operand_one + operand_two
                elif t == "-":
                    res = operand_one - operand_two
                elif t == "*":
                    res = operand_one * operand_two
                else:
                    res = int(operand_one / operand_two)
                stack.append(res)
        return stack[-1]
            