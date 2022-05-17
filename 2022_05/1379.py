from typing import Optional
from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if target is original: return cloned
        p = self.find(original, target, [])
        t = cloned
        for p in p:
            if p == 0:
                t = t.left
            elif p == 1:
                t = t.right
        return t

    def find(self, r, t, p):
        if r.left is t: return p + [0]
        if r.right is t: return p + [1]
        if r.left is not None:
            a = self.find(r.left, t, p + [0])
            if a is not None: return a
        if r.right is not None:
            a = self.find(r.right, t, p + [1])
            if a is not None: return a
        return None

    def convert_input(self, l):
        r = TreeNode(l[0])
        q = Queue()
        q.put(r)
        i = 1
        while i < len(l):
            a = q.get(False)
            t = l[i]
            if t is None:
                a.left = None
            else:
                a.left = TreeNode(t)
                q.put(a.left)
            i += 1
            t = l[i]
            if t is None:
                a.right = None
            else:
                a.right = TreeNode(t)
                q.put(a.right)
            i += 1
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

    def get_target(self, r, t):
        if r.val == t: return r
        if r.left is not None:
            a = self.get_target(r.left, t)
            if a is not None: return a
        if r.right is not None:
            a = self.get_target(r.right, t)
            if a is not None: return a
        return None

    def wrap(self, tree, target):
        r = self.convert_input(tree)
        a = self.convert_input(tree)
        # l = self.convert_output(r)
        t = self.get_target(r, target)
        t = self.getTargetCopy(r, a, t)
        return t.val


if __name__ == '__main__':
    solution = Solution()
    print(solution.wrap(tree=[7,4,3,None,None,6,19], target=3))
    print(solution.wrap(tree=[8,None,6,None,5,None,4,None,3,None,2,None,1], target=4))
