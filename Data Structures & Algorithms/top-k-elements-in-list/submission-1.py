class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hashmap with count of numbers
        count = defaultdict(list)
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        arr = []
        # returns list of hashmap
        for key, value in count.items():
            arr.append([value, key])
        # sorted by highest frequency
        arr.sort()

        result = []
        while len(result) < k:
            # pops value and appends the key to result
            result.append(arr.pop()[1])
        return result



