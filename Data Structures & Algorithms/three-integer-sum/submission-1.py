class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result: set[tuple[int, int, int]] = set()
        nums.sort()

        for i in range(len(nums)):
            left_pos: int = i + 1
            right_pos: int = len(nums) - 1

            while left_pos < right_pos:
                total: int = nums[i] + nums[left_pos] + nums[right_pos]
                if total == 0:
                    result.add((nums[i], nums[left_pos], nums[right_pos]))
                    left_pos += 1
                    right_pos -= 1
                elif total < 0:
                    left_pos += 1
                else:
                    right_pos -= 1

        return [list(triplet) for triplet in result]