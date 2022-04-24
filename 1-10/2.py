from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def wrap(self, l1, l2):
        l1 = self.convert_input(l1); l2 = self.convert_input(l2)
        l = self.addTwoNumbers(l1, l2)
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

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        h = l = ListNode()
        while not (l1 is None and l2 is None and c == 0):
            if l1 is not None:
                c += l1.val
                l1 = l1.next
            if l2 is not None:
                c += l2.val
                l2 = l2.next
            l.next = ListNode(c % 10)
            l = l.next
            c = c // 10
        return h.next


if __name__ == '__main__':
    solution = Solution()
    print(solution.wrap(l1=[2,4,3], l2=[5,6,4]))
    print(solution.wrap(l1=[9,9,9,9,9,9,9], l2=[9,9,9,9]))
