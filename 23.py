from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0: return None
        if n == 1: return lists[0]
        if n > 2:
            n //= 2
            lists = [self.mergeKLists(lists[:n]), self.mergeKLists(lists[n:])]
        p1, p2 = lists
        d = h = ListNode()
        while not (p1 is None or p2 is None):
            if p1.val <= p2.val:
                h.next = p1
                p1 = p1.next
            else:
                h.next = p2
                p2 = p2.next
            h = h.next
        if p1 is not None:
            h.next = p1
        elif p2 is not None:
            h.next = p2
        return d.next

    def wrap(self, lists):
        l = [self.convert_input(l) for l in lists]
        l = self.mergeKLists(l)
        return self.convert_output(l)

    def convert_input(self, l):
        l.reverse()
        p = None
        for a in l:
            p = ListNode(a, p)
        return p

    def convert_output(self, l):
        r = []
        while l is not None:
            r.append(l.val)
            l = l.next
        return r


if __name__ == '__main__':
    solution = Solution()
    print(solution.wrap(lists=[[1,4,5],[1,3,4],[2,6]]))
    print(solution.wrap(lists=[]))
