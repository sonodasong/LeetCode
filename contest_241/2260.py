from typing import List


class Solution:

    def countPrefixes(self, cards: List[int]) -> int:
        d = {}
        for i, c in enumerate(cards):
            if c in d:
                d[c].append(i)
            else:
                d[c] = [i]
        l = []
        for k in d:
            t = d[k]; n = len(t)
            if len(t) <= 1: continue
            l.append(min([t[i + 1] - t[i] for i in range(n - 1)]) + 1)
        if len(l) == 0: return -1
        return min(l)


if __name__ == '__main__':
    solution = Solution()
    print(solution.countPrefixes(cards=[3,4,2,3,4,7]))
    print(solution.countPrefixes(cards=[1,0,5,3]))
