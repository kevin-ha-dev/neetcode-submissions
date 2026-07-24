class MinStack:

    def __init__(self):
        self.stack: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        tmp_stack: list[int] = []
        min_value: int = self.stack[-1]

        while len(self.stack):
            min_value = min(min_value, self.stack[-1])
            tmp_stack.append(self.stack.pop())

        while len(tmp_stack):
            self.stack.append(tmp_stack.pop())
        
        return min_value 

