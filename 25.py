from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head
        n = 0
        h = head
        while h is not None:
            n += 1
            h = h.next
        d = p = b = ListNode(None, head); q = head
        for _ in range(n // k):
            a = b; b = q
            for _ in range(k):
                t = q.next
                q.next = p
                p = q
                q = t
            a.next = p; b.next = q
        return d.next

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

    def wrap(self, head, k):
        head = self.convert_input(head)
        l = self.reverseKGroup(head, k)
        return self.convert_output(l)


if __name__ == '__main__':
    solution = Solution()
    print(solution.wrap(head=[1,2,3,4,5], k=2))
    print(solution.wrap(head=[1,2,3,4,5], k=3))
