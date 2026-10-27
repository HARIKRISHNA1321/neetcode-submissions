class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x=""
        
        y=0
        z=0
        for i in range(len(s)):
            if s[i] not in x:
                x+=s[i]
                
                
            elif s[i] in x:
                h=x.index(s[i])
                x=x[(h+1)::]
                x+=s[i]
            y=len(x)
            if y>z:
                z=y
        
        
        
        
        return z


        