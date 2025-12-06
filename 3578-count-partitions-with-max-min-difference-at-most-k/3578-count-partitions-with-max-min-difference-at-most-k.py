class Solution:
    def countPartitions(self, nums, k):
        n=len(nums)
        MOD=10**9+7

        sum=[0]*(n+2)
        sum[1]=1

        qMax=deque()  
        qMin=deque() 

        l=0
        cnt=0

        for r, x in enumerate(nums):

            # max queue 
            while qMax and qMax[-1]<x:
                qMax.pop()
            qMax.append(x)

            # min queue 
            while qMin and qMin[-1]>x:
                qMin.pop()
            qMin.append(x)

            # shrink window
            while qMax[0]-qMin[0]>k:
                y=nums[l]
                if qMax[0]==y:
                    qMax.popleft()
                if qMin[0]==y:
                    qMin.popleft()
                l+=1

            #  update cnt & sum[r+2]
            cnt=(sum[r+1]-sum[l])%MOD
            sum[r+2]=(sum[r+1]+cnt)%MOD

        return cnt
    