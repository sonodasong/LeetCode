from typing import Optional
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = Queue()
        q.put((root, 0))
        l = []
        index = 0
        while q.qsize() > 0:
            r, i = q.get(False)
            if i > index:
                l = []
                index = i
            l.append(r.val)
            if r.left is not None:
                q.put((r.left, i + 1))
            if r.right is not None:
                q.put((r.right, i + 1))
        return sum(l)

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

    def wrap(self, root):
        r = self.convert_input(root)
        # l = self.convert_output(r)
        return self.deepestLeavesSum(r)


if __name__ == '__main__':
    solution = Solution()
    print(solution.wrap(root=[1,2,3,4,5,None,6,7,None,None,None,None,8]))
    print(solution.wrap(root=[6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]))
