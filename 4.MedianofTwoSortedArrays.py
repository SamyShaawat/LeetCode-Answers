class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_array = sorted(nums1 + nums2)

        size = len(merged_array)
        if size % 2 == 0:
            median = (merged_array[(size // 2) - 1] + merged_array[(size // 2)]) / 2.0
        else:
            median = merged_array[size // 2]

        return median
