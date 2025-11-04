class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def x_sum(freq):
            freq2=sorted(freq, reverse=True)
            Sum=0
            for f, num in freq2[:x]:
                if f==0: break
                Sum+=num*f
            return Sum
        n=len(nums)
        sz=n-k+1
        ans=[0]*sz
        freq=[[0, 0] for _ in range(51)]
        for z in nums[:k]:
            freq[z][1]=z
            freq[z][0]+=1
        ans[0]=x_sum(freq)
        for l in range(1, sz):
            L, R=nums[l-1], nums[l+k-1]
            freq[L][0]-=1
            freq[R][0]+=1
            freq[R][1]=R
            ans[l]=x_sum(freq)
        return ans
        