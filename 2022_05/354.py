from typing import List
from bisect import bisect_left


class Solution:

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        wd = {}
        wl = []
        for a, b in envelopes:
            if a in wd:
                wd[a].add(b)
            else:
                wd[a] = {b}
                wl.append(a)
        for k in wd:
            wd[k] = sorted(wd[k], reverse=True)
        wl.sort()
        h = []
        for w in wl:
            for x in wd[w]:
                i = bisect_left(h, x)
                if i == len(h):
                    h.append(x)
                else:
                    h[i] = x
        return len(h)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxEnvelopes(envelopes=[[5,4],[6,4],[6,7],[2,3]]))
    print(solution.maxEnvelopes(envelopes=[[1,1],[1,1],[1,1]]))
    print(solution.maxEnvelopes(envelopes=[[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]))
    print(solution.maxEnvelopes(envelopes=[[10,4],[13,18],[1,5],[13,15],[3,12],[12,11],[17,15],[7,1],[17,18],[7,19],[2,5],[8,9],[18,10],[7,6],[17,7]]))
