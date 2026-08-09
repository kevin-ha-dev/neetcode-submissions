class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pos: int = 0
        right_pos: int = len(heights) - 1
        max_area: int = 0

        while left_pos < right_pos:
            min_height: int = min(heights[left_pos], heights[right_pos])
            current_area: int = (right_pos - left_pos) * min_height
            max_area = max(current_area, max_area)

            if heights[left_pos] < heights[right_pos]:
                left_pos += 1
            else:
                right_pos -= 1
        
        return max_area