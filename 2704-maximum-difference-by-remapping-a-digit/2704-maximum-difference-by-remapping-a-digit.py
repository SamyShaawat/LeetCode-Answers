class Solution:
    def minMaxDifference(self, num: int) -> int:
        string = str(num)
        print(type(string))
        min_s = string
        max_s = string
        for ch in string:
            if ch != '9':
                max_s = string.replace(ch, '9')
                break


        for ch in string:
            if ch != '0':
                min_s = string.replace(ch, '0')
                break
        return int(max_s) - int(min_s)