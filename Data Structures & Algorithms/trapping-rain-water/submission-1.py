class Solution:
    def trap(self, height: List[int]) -> int:
        total_water: int = 0
        left: int = 0
        right: int = len(height) - 1

        left_max: int = 0
        right_max: int = 0

        while left < right:  

            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                curr_water: int = left_max - height[left]
                total_water += curr_water
                left += 1
            else:
                right_max = max(right_max, height[right])
                curr_water: int= right_max - height[right]
                total_water += curr_water
                right -= 1
        return total_water

            