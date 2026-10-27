class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x=""
        n=[]
        y=0
        for i in range(len(s)):
            if s[i] not in x:
                x+=s[i]
                
                
            elif s[i] in x:
                h=x.index(s[i])
                x=x[(h+1)::]
                x+=s[i]
            y=len(x)
            n.append(y)
        
        
        if len(n)!=0:
            z=max(n)
        else:
            z=0
        
        return z


        