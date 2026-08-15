class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target: dict[str, int] = {}
        window: dict[str, int] = {}
        left: int = 0

        for char in s1:
            target[char] = target.get(char, 0) + 1

        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1

            while (right - left + 1) > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            if window == target:
                return True

        return False