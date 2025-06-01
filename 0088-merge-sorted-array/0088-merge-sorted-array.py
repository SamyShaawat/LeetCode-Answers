class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Create a temporary list to hold merged elements
        merged = []
        i, j = 0, 0

        # Traverse through nums1 and nums2 and merge their elements
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        # Append any leftover elements in nums1
        while i < m:
            merged.append(nums1[i])
            i += 1

        # Append any leftover elements in nums2
        while j < n:
            merged.append(nums2[j])
            j += 1

        # Copy elements back to nums1
        for k in range(m + n):
            nums1[k] = merged[k]