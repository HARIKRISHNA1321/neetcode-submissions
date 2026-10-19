class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        x=0
        y=0
        n=len(nums)
        ans=[]
        for i in range(n):
            if i==0:
                x=nums[i]
            else:
                x*=nums[i]
            a.append(x)
        for i in range(n):
            if -(i+1)==-1:
                y=nums[-1]
            else:
                y*=nums[-(i+1)]
            b.append(y)
        
        for i in range(n):
            if i==0:
                ans.append(b[-2])
            elif i==(n-1):
                ans.append(a[-2])
            else:
                ans.append(a[i-1]*b[-(i+2)])
        return ans
        

        



        