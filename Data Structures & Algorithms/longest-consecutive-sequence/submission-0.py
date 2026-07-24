class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset: set[int] = set(nums)
        longest_sequence: int = 0

        for num in nums:
            if num - 1 not in numset:
                current_num: int = num
                current_sequence: int = 0
                while current_num in numset:
                    current_num += 1
                    current_sequence += 1
                    longest_sequence = max(current_sequence, longest_sequence)
        return longest_sequence
