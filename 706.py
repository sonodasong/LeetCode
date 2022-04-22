class MyHashMap:

    def __init__(self):
        N = 10007
        self.a = [None] * N
        self.b = [0] * N
        self.N = N

    def h(self, k):
        return k % self.N

    def put(self, key: int, value: int) -> None:
        a = self.a; b = self.b; N = self.N
        k = self.get_hash(key)
        if k >= 0:
            if a[k][1] == value: return
            a[k] = (key, value)
            return
        k = self.h(key)
        i = 1
        while a[k] is not None:
            b[k] += 1
            k += i ** 2
            k %= N
            i += 1
        a[k] = (key, value)

    def remove(self, key: int) -> None:
        if self.get_hash(key) < 0: return
        a = self.a; b = self.b; N = self.N
        k = self.h(key)
        i = 1
        while not (a[k] is None and b[k] == 0):
            if a[k] and a[k][0] == key:
                a[k] = None
                return
            else:
                b[k] -= 1
            k += i ** 2
            k %= N
            i += 1

    def get_hash(self, key):
        a = self.a; b = self.b; N = self.N
        k = self.h(key)
        i = 1
        while not (a[k] is None and b[k] == 0):
            if a[k] and a[k][0] == key: return k
            k += i ** 2
            k %= N
            i += 1
        return -1

    def get(self, key: int) -> int:
        k = self.get_hash(key)
        if k < 0: return -1
        return self.a[k][1]


if __name__ == '__main__':
    myHashMap = MyHashMap()
    print(myHashMap.put(1, 1)) # The map is now [[1,1]]
    print(myHashMap.put(2, 2)) # The map is now [[1,1], [2,2]]
    print(myHashMap.get(1))    # return 1, The map is now [[1,1], [2,2]]
    print(myHashMap.get(3))    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
    print(myHashMap.put(2, 1)) # The map is now [[1,1], [2,1]] (i.e., update the existing value)
    print(myHashMap.get(2))    # return 1, The map is now [[1,1], [2,1]]
    print(myHashMap.remove(2)) # remove the mapping for 2, The map is now [[1,1]]
    print(myHashMap.get(2))    # return -1 (i.e., not found), The map is now [[1,1]]
