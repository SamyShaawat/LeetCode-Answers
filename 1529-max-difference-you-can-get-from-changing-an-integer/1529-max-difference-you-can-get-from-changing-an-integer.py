class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)

        for d in s:
            if d != '9':
                max_num = int(s.replace(d, '9'))
                break
        else:
            max_num = num  
        
        if s[0] != '1':
            min_num = int(s.replace(s[0], '1'))
        else:
            for d in s[1:]:
                if d not in ['0', '1']:
                    min_num = int(s.replace(d, '0'))
                    break
            else:
                min_num = num 
        
        return max_num - min_num
