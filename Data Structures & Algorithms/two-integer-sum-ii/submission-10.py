class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        l1=[]
        while len(l1)==0:
            if numbers[l]+numbers[r]==target:
                l1.append(l+1)
                l1.append(r+1)
            elif numbers[l]+numbers[r]<target:
                l+=1
            else:
                r-=1
        return l1
                

        