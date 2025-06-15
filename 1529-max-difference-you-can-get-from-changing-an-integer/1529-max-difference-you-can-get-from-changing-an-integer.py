class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        
        # Generate max number: replace first digit that is not '9' with '9'
        for d in s:
            if d != '9':
                max_num = int(s.replace(d, '9'))
                break
        else:
            max_num = num  # All digits are '9'
        
        # Generate min number:
        # Case 1: if first digit != '1', replace it with '1'
        # Case 2: otherwise, find first digit != '0' and != '1', and replace it with '0'
        if s[0] != '1':
            min_num = int(s.replace(s[0], '1'))
        else:
            for d in s[1:]:
                if d not in ['0', '1']:
                    min_num = int(s.replace(d, '0'))
                    break
            else:
                min_num = num  # No suitable digit found
        
        return max_num - min_num
