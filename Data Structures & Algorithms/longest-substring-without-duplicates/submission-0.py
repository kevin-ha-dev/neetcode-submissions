class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen: set[char] = set()
        i: int = 0
        max_length: int = 0

        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            max_length = max(max_length, j - i + 1)
                
        return max_length