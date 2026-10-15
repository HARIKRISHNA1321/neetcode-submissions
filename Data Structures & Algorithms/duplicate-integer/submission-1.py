class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count =0
        nums=sorted(nums)
        for i in range(len(nums)-1):
            if (nums[i]==nums[i+1]):
                count+=1
        if count>0:
            return True
        else:
            return False
