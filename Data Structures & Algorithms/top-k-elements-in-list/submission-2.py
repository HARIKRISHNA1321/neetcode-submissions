class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        for x in nums:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1
   

        l1=sorted(dict1.items(),key= lambda item: item[1], reverse=True)
        l2=[x[0] for x in l1[:k] ]
        return l2
        
        