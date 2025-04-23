class Solution:
    def countLargestGroup(self, n: int) -> int:
        dict_count = defaultdict (int)
        for i in range(1, n+1) : 
            count = 0 
            for j in str(i) : 
                count += int(j) 

            dict_count[count] += 1 

       # print (dict_count)

        mx = max(dict_count.values())
       #print (mx)
        c = 0 
        for i in dict_count.values() : 
            if(i == mx) : 
                c+=1 
        return c