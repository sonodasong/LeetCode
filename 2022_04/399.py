from typing import List


class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = {}
        # l = []
        for (a, b), v in zip(equations, values):
            # self.add(dic, l, a, b, v)
            self.add(dic, a, b, v)
        l = []
        for a, b in queries:
            if a not in dic:
                l.append(-1.0)
                continue
            if b not in dic:
                l.append(-1.0)
                continue
            da = dic[a]; db = dic[b]
            if da is not db:
                l.append(-1.0)
                continue
            l.append(da[a] / db[b])
        return l

    # def add(self, dic, l, a, b, v):
    #     if a in dic and b in dic:
    #         da, ra = dic[a]; db, rb = dic[b]
    #         if da is db: return
    #         if len(da) > len(db):
    #             t = dic[a]; r = da[a] / db[b]
    #             for k in db:
    #                 da[k] = r / v * db[k]
    #                 dic[k] = t
    #             l.remove(rb)
    #         else:
    #             t = dic[b]; r = db[b] / da[a]
    #             for k in da:
    #                 db[k] = r * v * da[k]
    #                 dic[k] = t
    #             l.remove(ra)
    #     elif a in dic:
    #         d, _ = dic[a]
    #         d[b] = d[a] / v
    #         dic[b] = dic[a]
    #     elif b in dic:
    #         d, _ = dic[b]
    #         d[a] = d[b] * v
    #         dic[a] = dic[b]
    #     else:
    #         d = ({b: 1, a: v}, b)
    #         l.append(b)
    #         dic[a] = d; dic[b] = d

    def add(self, dic, a, b, v):
        if a in dic and b in dic:
            da = dic[a]; db = dic[b]
            if da is db: return
            if len(da) > len(db):
                r = da[a] / db[b]
                for k in db:
                    da[k] = r / v * db[k]
                    dic[k] = da
            else:
                r = db[b] / da[a]
                for k in da:
                    db[k] = r * v * da[k]
                    dic[k] = db
        elif a in dic:
            d = dic[a]
            d[b] = d[a] / v
            dic[b] = d
        elif b in dic:
            d = dic[b]
            d[a] = d[b] * v
            dic[a] = d
        else:
            d = {b: 1, a: v}
            dic[a] = d; dic[b] = d


if __name__ == '__main__':
    solution = Solution()
    print(solution.calcEquation(equations=[['a','b'],['b','c']], values=[2.0,3.0], queries=[['a','c'],['b','a'],['a','e'],['a','a'],['x','x']]))
    print(solution.calcEquation(equations=[['a','b'],['b','c'],['bc','cd']], values=[1.5,2.5,5.0], queries=[['a','c'],['c','b'],['bc','cd'],['cd','bc']]))
    print(solution.calcEquation(equations=[['a','b']], values=[0.5], queries=[['a','b'],['b','a'],['a','c'],['x','y']]))
