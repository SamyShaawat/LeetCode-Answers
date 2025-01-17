class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # first sol:
        # valid = 0
        # for i in derived:
        #     valid = valid ^ i 
        # if valid == 0:
        #     return True 
        # else:
        #     return False
        # second sol:
        n = sum(derived)
        if n % 2 == 0:
            return True
        else:
            return False
        