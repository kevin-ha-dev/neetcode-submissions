class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []

        closeToOpen: dict[str, str] = { 
        ")": "(",
        "]": "[",
        "}": "{"
        }

        for char in s: 
            if char in closeToOpen:
                if len(stack) == 0:
                    return False
                if stack[-1] != closeToOpen[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
