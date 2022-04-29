from typing import List


class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        d = {}
        l = []
        for x, y in pairs:
            a = x in d
            b = y in d
            if a and b:
                if d[x] is not d[y]:
                    if len(d[x][0]) < len(d[y][0]):
                        t = d[y]
                        t[0].update(d[x][0])
                        l.remove(d[x][1])
                        for x in d[x][0]:
                            d[x] = t
                    else:
                        t = d[x]
                        t[0].update(d[y][0])
                        l.remove(d[y][1])
                        for y in d[y][0]:
                            d[y] = t
            elif a:
                d[x][0].add(y)
                d[y] = d[x]
            elif b:
                d[y][0].add(x)
                d[x] = d[y]
            else:
                t = [set((x, y)), x]
                l.append(x)
                d[x] = t; d[y] = t
        s = [c for c in s]
        for a in l:
            a = d[a][0]
            t = sorted([s[i] for i in a])
            for i, c in enumerate(sorted(list(a))):
                s[c] = t[i]
        return ''.join(s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.smallestStringWithSwaps(s='dcab', pairs=[[0,3],[1,2]]))
    print(solution.smallestStringWithSwaps(s='dcab', pairs=[[0,3],[1,2],[0,2]]))
