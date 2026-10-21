class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        num=sorted(list(num))
        x=0
        count=0
        for i in range(0,len(num)):
            if i==0:
                count+=1
            if num[i-1]+1==num[i]:
                count+=1
            else:
                count=1
            if count>x:
                x=count
        return x
            


        