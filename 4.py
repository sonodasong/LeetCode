from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1); n2 = len(nums2)
        i1 = n1 // 2; i2 = (n1 + n2) // 2 - i1
        l = 0; r = n1
        d = self.check(nums1, n1, i1, nums2, n2, i2)
        while not d == 0:
            if d > 0:
                l = i1
                c = (min(r - i1, i2) + 1) // 2
                i1 += c; i2 -= c
            else:
                r = i1
                c = (min(i1 - l, n2 - i2) + 1) // 2
                i1 -= c; i2 += c
            d = self.check(nums1, n1, i1, nums2, n2, i2)
        if (n1 + n2) % 2 == 0:
            return (self.get_lm(nums1, i1, nums2, i2) + self.get_rm(nums1, n1, i1, nums2, n2, i2)) / 2
        else:
            return self.get_rm(nums1, n1, i1, nums2, n2, i2)

    def check(self, nums1, n1, i1, nums2, n2, i2):
        if i1 > 0 and i2 < n2 and nums1[i1 - 1] > nums2[i2]: return -1
        if i2 > 0 and i1 < n1 and nums2[i2 - 1] > nums1[i1]: return 1
        return 0

    def get_lm(self, nums1, i1, nums2, i2):
        if i1 == 0: return nums2[i2 - 1]
        if i2 == 0: return nums1[i1 - 1]
        return max(nums1[i1 - 1], nums2[i2 - 1])

    def get_rm(self, nums1, n1, i1, nums2, n2, i2):
        if i1 == n1: return nums2[i2]
        if i2 == n2: return nums1[i1]
        return min(nums1[i1], nums2[i2])


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1=[], nums2=[1]))
    print(solution.findMedianSortedArrays(nums1=[1], nums2=[1]))
    print(solution.findMedianSortedArrays(nums1=[2,3,4], nums2=[1]))
    print(solution.findMedianSortedArrays(nums1=[2,3], nums2=[1]))
    print(solution.findMedianSortedArrays(nums1=[3,4], nums2=[1,2,5]))
    print(solution.findMedianSortedArrays(nums1=[1,2,5], nums2=[3,4,6]))
    print(solution.findMedianSortedArrays(nums1=[1,3], nums2=[2]))
    print(solution.findMedianSortedArrays(nums1=[1,2], nums2=[3,4]))
