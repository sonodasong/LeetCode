# class MyHashSet:

#     def __init__(self):
#         self.a = set()

#     def add(self, key: int) -> None:
#         self.a.add(key)

#     def remove(self, key: int) -> None:
#         if key in self.a:
#             self.a.remove(key)

#     def contains(self, key: int) -> bool:
#         return key in self.a


class MyHashSet:

    def __init__(self):
        N = 10007
        self.a = [None] * N
        self.b = [0] * N
        self.N = N

    def h(self, k):
        return k % self.N

    def add(self, key: int) -> None:
        if self.contains(key): return
        a = self.a; b = self.b; N = self.N
        k = self.h(key)
        i = 1
        while a[k] is not None:
            b[k] += 1
            k += i ** 2
            k %= N
            i += 1
        a[k] = key

    def remove(self, key: int) -> None:
        if not self.contains(key): return
        a = self.a; b = self.b; N = self.N
        k = self.h(key)
        i = 1
        while not (a[k] is None and b[k] == 0):
            if a[k] == key:
                a[k] = None
                return
            else:
                b[k] -= 1
            k += i ** 2
            k %= N
            i += 1

    def contains(self, key: int) -> bool:
        a = self.a; b = self.b; N = self.N
        k = self.h(key)
        i = 1
        while not (a[k] is None and b[k] == 0):
            if a[k] == key: return True
            k += i ** 2
            k %= N
            i += 1
        return False


if __name__ == '__main__':
    myHashSet = MyHashSet()
    print(myHashSet.add(1))      # set = [1]
    print(myHashSet.add(1))      # set = [1]
    print(myHashSet.add(2))      # set = [1, 2]
    print(myHashSet.contains(1)) # return True
    print(myHashSet.contains(3)) # return False, (not found)
    print(myHashSet.add(2))      # set = [1, 2]
    print(myHashSet.contains(2)) # return True
    print(myHashSet.remove(2))   # set = [1]
    print(myHashSet.contains(2)) # return False, (already removed)
