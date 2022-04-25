from typing import List


# class Solution:

#     def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
#         p = list(set(persons))
#         d = {}
#         for person in persons:
#             d[person] = 0
#         p = list(d.keys())
#         p.sort()
#         for x, y in flowers:
#             for i in range(self.lbs(p, x), self.rbs(p, y)):
#                 d[p[i]] += 1
#         return [d[person] for person in persons]

#     def lbs(self, a, x):
#         if x <= a[0]: return 0
#         n = len(a)
#         if x > a[-1]: return n
#         l = 0; r = n
#         while True:
#             m = (l + r) // 2
#             if a[m] == x:
#                 if m - l == 1: return m
#                 r = m
#             elif r - l == 1:
#                 return m + 1
#             elif a[m] > x:
#                 r = m
#             elif a[m] < x:
#                 l = m

#     def rbs(self, a, x):
#         m = self.lbs(a, x)
#         # need to rewrite rbs
#         # if m < len(a) and a[m] == x: return m + ?
#         if m < len(a) and a[m] == x: return m + 1
#         return m

#     def bs(self, a, x):
#         l = 0; r = len(a)
#         while True:
#             m = (l + r) // 2
#             if a[m] == x: return True
#             if r - l == 1: return False
#             if a[m] > x:
#                 r = m
#             elif a[m] < x:
#                 l = m


# class Solution:

#     def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
#         d = {}
#         for x, y in flowers:
#             if y in d:
#                 d[y].append(x)
#             else:
#                 d[y] = [x]
#         for k in d:
#             d[k].sort()
#         y = list(d.keys())
#         y.sort()
#         l = {}
#         for p in set(persons):
#             a = 0
#             for i in y[self.lbs(y, p):]:
#                 t = d[i]
#                 a += self.rbs(t, p)
#             l[p] = a
#         return [l[p] for p in persons]

#     def lbs(self, a, x):
#         if x <= a[0]: return 0
#         n = len(a)
#         if x > a[-1]: return n
#         l = 0; r = n
#         while True:
#             m = (l + r) // 2
#             if a[m] == x:
#                 if m - l == 1: return m
#                 r = m
#             elif r - l == 1:
#                 return m + 1
#             elif a[m] > x:
#                 r = m
#             elif a[m] < x:
#                 l = m

#     def rbs(self, a, x):
#         return self.lbs(a, x + 1)

#     def index_sort(self, l):
#         m = max(l); D = 0
#         while m > 0:
#             D += 1
#             m //= 10
#         n = len(l)
#         l1 = l; l2 = [0] * n; i2 = 0
#         for d in range(D):
#             r = [(x % 10 ** (d + 1)) // (10 ** d) for x in l1]
#             for k in range(10):
#                 for i1 in range(n):
#                     if r[i1] == k:
#                         l2[i2] = l1[i1]; i2 += 1
#             t = l1; l1 = l2; l2 = t; i2 = 0
#         return l1


class Solution:

    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        n = len(flowers)
        x = [x for x, _ in flowers]
        y = [y for _, y in flowers]
        x.sort()
        y.sort()
        d = {}
        for p in set(persons):
            # n - self.lbs(x + 1, p)
            # self.lbs(y, p)
            d[p] = self.lbs(x, p + 1) - self.lbs(y, p)
        return [d[p] for p in persons]

    def lbs(self, a, x):
        if x <= a[0]: return 0
        n = len(a)
        if x > a[-1]: return n
        l = 0; r = n
        while True:
            m = (l + r) // 2
            if a[m] == x:
                if m - l == 1: return m
                r = m
            elif r - l == 1:
                return m + 1
            elif a[m] > x:
                r = m
            elif a[m] < x:
                l = m


if __name__ == '__main__':
    solution = Solution()
    print(solution.fullBloomFlowers(flowers=[[1,6],[3,7],[9,12],[4,13]], persons=[2,3,7,11]))
    print(solution.fullBloomFlowers(flowers=[[1,10],[3,3]], persons=[3,3,2]))
