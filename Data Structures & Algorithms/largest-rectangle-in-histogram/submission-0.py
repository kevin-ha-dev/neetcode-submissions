class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # The key here is when an element is popped because the previous was greated than current, we append to stack current with the previous elements index. Inheritance. From there we are able to calculate total area.

        stack: list[tuple[int, int]] = []
        max_area: int = 0

        for i, height in enumerate(heights):
            start: int = i
            while stack and height < stack[-1][1]:
                popped: tuple[int,int] = stack.pop()
                index: int = popped[0]
                popped_height: int = popped[1]
                
                area: int = popped_height * (i - index)
                max_area = max(max_area, area)
                start = index

            stack.append((start, height))
        
        # After we recieved final stack list we can start to calculate area for all i in stack

        for item in stack:
            start_index: int = item[0]
            remaining_height: int = item[1]

            remaining_area: int = remaining_height * (len(heights) - start_index)
            max_area = max(remaining_area, max_area)

        return max_area