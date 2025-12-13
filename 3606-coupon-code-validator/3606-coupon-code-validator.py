import re
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(isActive)
        business_order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        valid = []
        for c, b, a in zip(code, businessLine, isActive):
            if re.fullmatch(r'\w+', c) and b in business_order and a:
                valid.append((b, c))
        def sort_key(item):
            b, c = item
            return (business_order[b], c)
        valid.sort(key=sort_key)
        res = []
        for b, c in valid:
            res.append(c)
                
        return res
        
        