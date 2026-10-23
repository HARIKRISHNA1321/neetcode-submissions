class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        ans=[]

        for i in range(len(nums)):
            
            l=i+1
            r=len(nums)-1
            while l<r:
                l1=[]
                if nums[i]+nums[l]+nums[r]>0:
                    r-=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                elif nums[i]+nums[l]+nums[r]==0:
                    l1.append(nums[i])
                    l1.append(nums[l])
                    l1.append(nums[r])
                    l+=1
                    r-=1
                    if l1 not in ans:
                        ans.append(l1)
        return ans
            

                

            

        