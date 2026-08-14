class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left: int = 1
        right: int = max(piles)

        while left <= right: 
            middle: int = (left + right) // 2
            total_time: int = 0

            for pile in piles: 
                total_time += math.ceil(pile / middle)
            
            if total_time > h:
                left = middle + 1
            else:
                right = middle - 1
        return left