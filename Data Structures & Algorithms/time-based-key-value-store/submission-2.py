class TimeMap:

    def __init__(self):
        self.hash: dict[str, list[tuple[int, str]]] = {}

    # trick for this problem is to visualize the map and knowing how to access tuples 

    # store key into hash with element tuple(value, timestamp)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = [] 
        self.hash[key].append((timestamp, value))

    # checks if key exist else return ""
    # binary search for latest timestamp value
    # return the value associated with that timestamp 
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash:
            return ""
        
        values: list[tuple(int, str)] = self.hash[key]
        left: int = 0
        right: int = len(values) - 1
        result: str = ""
        
        while left <= right:
            mid: int = (left + right) // 2

            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return result
            
    
        
