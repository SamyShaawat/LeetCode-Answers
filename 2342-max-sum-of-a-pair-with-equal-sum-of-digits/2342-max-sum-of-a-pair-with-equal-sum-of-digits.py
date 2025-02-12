class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # 18 = 1 + 8 = 9
        # 43 = 4 + 3 = 7 
        # 36 = 3 + 6 = 9 
        # 13 = 1 + 3 = 4
        # 7  = 7     = 7

        # hashmap:
        # {
            # 9: [18, 36]
            # 7: [7, 43]
            # 4: [13]
        # } 

        # 123 % 10 = 3 
        # 123 // 10 = 12
        # 12 % 10 = 2
        # 12 // 10 = 1 
        # 1 % 10 = 1
        # 1 // 10 = 0

        hashmap = defaultdict(list)

        for num in nums: 
            t,temp =0, num
            while num:
                t += num%10 
                num //= 10
            hashmap[t].append(temp)
        # print(hashmap)
        res = -1
        for key in hashmap:
            # print(key)
            if len(hashmap[key])>= 2:
                res = max(res, sum(heapq.nlargest(2, hashmap[key])))
        return res


