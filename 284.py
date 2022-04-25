class Iterator:

    def __init__(self, nums):
        self.l = nums
        self.n = len(nums)
        self.i = -1

    def hasNext(self):
        return self.i < self.n - 1

    def next(self):
        self.i += 1
        return self.l[self.i]


class PeekingIterator:

    def __init__(self, iterator):
        self.iterator = iterator
        self.f = None

    def peek(self):
        if self.f is None:
            self.f = self.iterator.next()
        return self.f

    def next(self):
        if self.f is None: return self.iterator.next()
        a = self.f
        self.f = None
        return a

    def hasNext(self):
        if self.f is None: return self.iterator.hasNext()
        return True


if __name__ == '__main__':
    iterator = Iterator([1, 2, 3])
    peekingIterator = PeekingIterator(iterator)
    print(peekingIterator.next())    # return 1, the pointer moves to the next element [1,2,3].
    print(peekingIterator.peek())    # return 2, the pointer does not move [1,2,3].
    print(peekingIterator.next())    # return 2, the pointer moves to the next element [1,2,3]
    print(peekingIterator.next())    # return 3, the pointer moves to the next element [1,2,3]
    print(peekingIterator.hasNext()) # return False

