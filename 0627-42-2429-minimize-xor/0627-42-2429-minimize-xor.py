class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b1 = bin(num1)[2:]
        # print(b1)
        b2 = bin(num2).count('1')
        # print(b2) 
        result = ['0'] * max(len(b1), b2)
        for i in range(len(b1)):
            if b2 == 0:
                 break
            if b1[i] == '1':
                result[i] = '1'
                b2-=1

        for i in range(len(result)-1,-1,-1):
            if b2 == 0:
                 break
            if result[i] == '0':
                result[i] = '1'
                b2-=1

        # print(result)
        x = int(''.join(result),2)
        # print(x)
        return x
      