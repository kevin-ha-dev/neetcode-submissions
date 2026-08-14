class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left: int = 1
        right: int = max(piles)

        while left <= right: 
            eating_speed: int = (left + right) // 2
            total_time: int = 0

            for pile in piles: 
                total_time += math.ceil(pile / eating_speed)
            
            if total_time > h:
                left = eating_speed + 1
            else:
                right = eating_speed - 1
        return left