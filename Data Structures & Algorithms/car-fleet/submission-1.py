class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars: list[tuple[int, int]] = sorted(zip(position, speed))
        total_fleet: int = 0
        prev_time: int = 0

        for i in range(len(cars) - 1, -1, -1):
            
            time: int = (target - cars[i][0]) / cars[i][1]

            if total_fleet == 0 or time > prev_time:
                total_fleet += 1
                prev_time = time
        
        return total_fleet