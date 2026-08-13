class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars: list[tuple[int, int]] = sorted(zip(position, speed))

        fleet: list[int] = []

        for i in range(len(cars) - 1, -1, -1):
            curr_position: int = cars[i][0]
            curr_speed: int = cars[i][1]
            time: int = (target - curr_position) / curr_speed

            if not fleet or time > fleet[-1]:
                fleet.append(time)
        
        return len(fleet)