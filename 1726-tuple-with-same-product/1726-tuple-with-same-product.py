class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_counts = {}
      
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prod = nums[i] * nums[j]
                if prod in product_counts:
                    product_counts[prod] += 1
                else:
                    product_counts[prod] = 1
        
        total_tuples = 0
        
        for y in product_counts.values():
            if y > 1:
                total_tuples += math.comb(y, 2) * 8      
        return total_tuples
