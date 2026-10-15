class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums=(nums)
        l1=[]
        for i in range(len(nums)):
            result=target-nums[i]
            if ((result) in nums) and (nums.index(result)!=i) :
                l1.append(i)
                l1.append(nums.index(result))
                break
                
        return sorted(l1)
                
                
        