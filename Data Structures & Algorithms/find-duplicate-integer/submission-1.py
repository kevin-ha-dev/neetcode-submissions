class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Use slow and fast pointers to detect cycle
        # Reset slow back to 0 and when slow == fast, is where our  duplicate is
        
        slow: int = 0
        fast: int = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
