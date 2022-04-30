from typing import List


class Solution:

    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.graph = graph
        self.check = [False] * len(graph)
        a = set()
        b = set()
        while False in self.check:
            i = self.check.index(False)
            if len(graph) == 0: continue
            if not self.add(i, a, b): return False
        return True

    def add(self, node, cur, other):
        check = self.check
        if check[node]: return True
        if node in cur: return False
        cur.add(node)
        for n in self.graph[node]:
            if n in cur: return False
        check[node] = True
        for node in self.graph[node]:
            if check[node]: continue
            if not self.add(node, other, cur): return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isBipartite(graph=[[1,2,3],[0,2],[0,1,3],[0,2]]))
    print(solution.isBipartite(graph=[[1,3],[0,2],[1,3],[0,2]]))
