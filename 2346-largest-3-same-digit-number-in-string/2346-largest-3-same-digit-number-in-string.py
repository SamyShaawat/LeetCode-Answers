class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9,-1, -1):
            check = (str(i)*3)
            if check in num:
                return check
        return ""
        # good_integer =['999', '888', '777', '666', '555', '444',
        #                 '333', '222', '111', '000']
        # for i in good_integer:
        #     if i in num:
        #         return i
        # return ""