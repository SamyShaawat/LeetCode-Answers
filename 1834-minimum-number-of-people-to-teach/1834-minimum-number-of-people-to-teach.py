class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        know=[]
        for L in languages:
            know.append(set(L))
        
        need=set()
        for a1, b1 in friendships:
            a, b=a1-1, b1-1
            if know[a] & know[b]: continue
            need.add(a)
            need.add(b)
        
        if not need: return 0

        ans=float('inf')
        for lang in range(1, n+1):
            cnt=0
            for i in need:
                if lang not in know[i]: cnt+=1
            ans=min(ans, cnt)
        return ans
        
        