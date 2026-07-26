class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: list[int] = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a: int = stack.pop()
                b: int = stack.pop()
                stack.append(b - a)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                a: int = stack.pop()
                b: int = stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(token))
        return stack[0]