from typing import List


class Solution:

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.i = 0
        v = [None] * n
        d = {}
        l = []
        for a, b in connections:
            if a in d:
                d[a].append(b)
            else:
                d[a] = [b]
            if b in d:
                d[b].append(a)
            else:
                d[b] = [a]
        self.find(v, d, l, None, 0)
        return l[:-1]

    def find(self, v, d, l, p, c):
        v[c] = self.i
        self.i += 1
        w = v[c]
        for t in d[c]:
            if t == p: continue
            if v[t] is None:
                w = min(w, self.find(v, d, l, c, t))
            else:
                w = min(w, v[t])
        if w == v[c]:
            l.append([p, c])
        return w


if __name__ == '__main__':
    solution = Solution()
    print(solution.criticalConnections(n=4, connections=[[0,1],[1,2],[2,0],[1,3]]))
    print(solution.criticalConnections(n=2, connections=[[0,1]]))
