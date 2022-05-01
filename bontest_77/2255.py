from typing import List


class Solution:

    def countPrefixes(self, words: List[str], s: str) -> int:
        a = 0
        for w in words:
            if s[:len(w)] == w:
                a += 1
        return a


if __name__ == '__main__':
    solution = Solution()
    print(solution.countPrefixes(words=['a','b','c','ab','bc','abc'], s='abc'))
