class Solution:
    def numSub(self, s: str) -> int:
        mod=10**9+7
        count=0
        ans=0
        for c in s:
            is0=c=='0'
            ans+=(-is0 & count*(count+1)//2)
            ans%=mod
            count=(-(not is0) & count+1)
        ans=ans+count*(count+1)//2%mod
        return ans

        