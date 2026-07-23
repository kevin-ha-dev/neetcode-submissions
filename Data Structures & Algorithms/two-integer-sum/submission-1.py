class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map: dict[int, int] = {} # val -> index

        for i, n in enumerate(nums): # i -> index n -> value
            difference = target - n
            if difference in map:
                return [map[difference], i]
            map[n] = i

        


        
