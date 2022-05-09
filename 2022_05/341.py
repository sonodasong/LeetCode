from __future__ import annotations


class NestedInteger:

    def __init__(self, l):
        if type(l) is int:
            self.i = l
            self.l = None
        else:
            self.i = None
            self.l = [NestedInteger(l) for l in l]

    def isInteger(self) -> bool:
        if self.i is not None: return True
        return False

    def getInteger(self) -> int:
        return self.i

    def getList(self) -> [NestedInteger]:
        return self.l


class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        self.l = [l.getInteger() if l.isInteger() else NestedIterator(l.getList()) for l in nestedList]
        self.n = len(self.l)
        self.i = 0

    def next(self) -> int:
        t = self.l[self.i]
        if type(t) is int:
            self.i += 1
            return t
        return t.next()

    def hasNext(self) -> bool:
        if self.i == self.n: return False
        t = self.l[self.i]
        if type(t) is int: return True
        if t.hasNext(): return True
        self.i += 1
        return self.hasNext()


if __name__ == '__main__':
    l = [[1,1],2,[1,1]]
    # l = [1,[4,[6]]]
    nestedList = [NestedInteger(l) for l in l]
    i, v = NestedIterator(nestedList), []
    while i.hasNext(): v.append(i.next())
    print(v)
