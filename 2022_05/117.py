from queue import Queue


class Node:

    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def connect(self, root: 'Node') -> 'Node':
        if root is None: return root
        h = root
        while h is not None:
            p = h
            h = t = None
            while p is not None:
                if p.left is not None:
                    if t is not None:
                        t.next = p.left
                    t = p.left
                    if h is None:
                        h = t
                if p.right is not None:
                    if t is not None:
                        t.next = p.right
                    t = p.right
                    if h is None:
                        h = t
                p = p.next
        return root

    def convert_input(self, n, i):
        index = 2 ** n - 1 + i
        l = self.l
        if index >= len(l): return None
        if l[index] is None: return None
        r = Node(l[index])
        r.left = self.convert_input(n + 1, i * 2)
        r.right = self.convert_input(n + 1, i * 2 + 1)
        return r

    def convert_output(self, r):
        l = []
        q = Queue()
        if r is not None:
            q.put(r)
        while q.qsize() > 0:
            r = q.get(False)
            l.append(r.val)
            if r.left is not None:
                q.put(r.left)
            if r.right is not None:
                q.put(r.right)
        return l

    def test(self, r):
        if r is None: return []
        l = []
        h = r
        while h is not None:
            p = h
            h = None
            while p is not None:
                l.append(p.val)
                if h is None:
                    if p.left is not None:
                        h = p.left
                    elif p.right is not None:
                        h = p.right
                p = p.next
            l.append('#')
        return l

    def wrap(self, root):
        self.l = root
        r = self.convert_input(0, 0)
        # l = self.convert_output(r)
        r = self.connect(r)
        return self.test(r)


if __name__ == '__main__':
    solution = Solution()
    print(solution.wrap(root=[1,2,3,4,5,None,7]))
    print(solution.wrap(root=[]))
