class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_prefix = max_prefix = curr = 0
        
        for diff in differences:
            curr += diff                      # build the prefix sum
            min_prefix = min(min_prefix, curr) # track the minimum prefix sum
            max_prefix = max(max_prefix, curr) # track the maximum prefix sum
        
        # if the range needed is bigger than available space, it's impossible
        if max_prefix - min_prefix > upper - lower:
            return 0
        
        # otherwise, count how many valid starting points we can have
        return (upper - lower) - (max_prefix - min_prefix) + 1