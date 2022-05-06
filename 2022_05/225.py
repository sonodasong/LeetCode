from queue import Queue


class MyStack:

    def __init__(self):
        self.q = Queue()
        self.t = None

    def push(self, x: int) -> None:
        q = self.q
        n = q.qsize()
        q.put(x)
        if self.t is not None:
            q.put(self.t)
            self.t = None
        for _ in range(n):
            q.put(q.get(False))

    def pop(self) -> int:
        if self.t is not None:
            t = self.t
            self.t = None
            return t
        return self.q.get(False)

    def top(self) -> int:
        if self.t is None:
            self.t = self.q.get(False)
        return self.t

    def empty(self) -> bool:
        if self.t is None:
            return self.q.qsize() == 0
        return False


if __name__ == '__main__':
    myStack =  MyStack()
    print(myStack.push(1))
    print(myStack.push(2))
    print(myStack.top()) # return 2
    print(myStack.pop()) # return 2
    print(myStack.empty()) # return False
