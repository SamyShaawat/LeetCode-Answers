class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # last pointer in the end of nums1 
        # m pointer points on  the last real number in nums1
        # n pointer points on  the last real number in nums2
        # get the last index in nums1 
        last = m + n - 1
        # merge in revese order
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n-= 1
            last -= 1
        while n > 0:
            nums1[last] = nums2[n-1]
            n, last = n-1, last-1


        