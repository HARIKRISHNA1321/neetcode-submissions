class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1=dict()
        for x in strs:
            y="".join(sorted(x))
            if y in dict1:
                dict1[y].append(x)
            else:
                dict1[y]=[x]
        z=list(dict1.values())    
        return z

            
            
        
        
        