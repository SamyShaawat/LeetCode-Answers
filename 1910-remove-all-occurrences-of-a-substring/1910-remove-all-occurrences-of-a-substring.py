class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "", 1)  # Removes the first occurrence of `part`
        return s
# another solution 
# class Solution:
#     def removeOccurrences(self, s: str, part: str) -> str:
#         while part in s:
#             for i in range(len(s) - len(part) +1): # explaing why exactly choose this range 
#                 window = s[i: i + len(part)] # here also why this range 
#                 if window == part:
#                     s = s.replace(window,"", 1) # what is replace do exactly 
#         return s  
