class Solution:
    def clearDigits(self, s: str) -> str:
        # fist solution using delete counter:
        # def isdigit(c):
        #     return ord("0") <= ord(c) <= ord("9")

        # result = []
        # delete_counter = 0

        # for i in reversed(range(len(s))):
        #     if s[i].isdigit():
        #         delete_counter +=1
        #     elif delete_counter:
        #         delete_counter -=1
        #     else:
        #         result.append(s[i])
        # return "".join(result[::-1])

        # second solution using delete stack:
        result = []
        for i in range(len(s)):
            if s[i].isdigit():
                result.pop()
            else:
                result.append(s[i])

        return "".join(result)

         
        
