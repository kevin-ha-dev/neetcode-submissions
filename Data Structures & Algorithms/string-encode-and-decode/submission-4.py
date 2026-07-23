class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s

        return result


    def decode(self, s: str) -> List[str]:
        result: list[str] = []
        i = 0

        while i < len(s):
            for j in range(i, len(s)):
                if s[j] == "#":
                    break
            length = int(s[i:j])
            word_start = j + 1
            word_end = word_start + length

            result.append(s[word_start:word_end])
            i = word_end
        return result
            
