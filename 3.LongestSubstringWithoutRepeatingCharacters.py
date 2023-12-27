# Given a string s, find the length of the longest substring without repeating characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        array = []
        max = 0
        for i in range(n):
            if s[i] not in array:
                array.append(s[i])
                if max < len(array):
                    max = len(array)
            else:
                array = []
        return max
