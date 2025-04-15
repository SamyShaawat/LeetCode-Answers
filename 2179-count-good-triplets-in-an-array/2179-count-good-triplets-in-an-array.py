class Solution:
    def goodTriplets(self, nums1, nums2):
        # Map each value in nums1 to its index
        value_to_index = {num: i for i, num in enumerate(nums1)}

        sorted_indices = []  # To keep track of the sorted indices in nums1
        total_triplets = 0

        for value in nums2:
            index_in_nums1 = value_to_index[value]

            # Count elements less than index_in_nums1 (left count)
            left_count = self._binary_search_insert_position(sorted_indices, index_in_nums1)

            # Calculate right count
            right_count = (len(nums1) - 1 - index_in_nums1) - (len(sorted_indices) - left_count)

            total_triplets += left_count * right_count

            # Insert the index in sorted order
            insert_pos = self._binary_search_insert_position(sorted_indices, index_in_nums1)
            sorted_indices.insert(insert_pos, index_in_nums1)

        return total_triplets

    # Helper function to find insertion position using binary search
    def _binary_search_insert_position(self, lst, target):
        low, high = 0, len(lst)

        while low < high:
            mid = (low + high) // 2
            if lst[mid] < target:
                low = mid + 1
            else:
                high = mid

        return low