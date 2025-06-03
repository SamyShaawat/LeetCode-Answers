class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        def dfs(i):
            ans=candies[i]
            status[i]=0
            for k in keys[i]:
                status[k]|=1
                if status[k]==3: ans+=dfs(k)
            for j in containedBoxes[i]:
                status[j]|=2
                if status[j]==3: ans+=dfs(j)
            return ans
        cnt=0
        for i in initialBoxes:
            status[i]|=2
            if status[i]==3:
                cnt+=dfs(i)
        return cnt