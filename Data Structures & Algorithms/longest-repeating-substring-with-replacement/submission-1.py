class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count: dict[str, int] = {}

        max_substring: int = 0

        left: int = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1 
                left += 1
            max_substring = max(max_substring, right - left + 1)
        
        return max_substring
