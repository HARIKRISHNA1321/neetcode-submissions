class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        count=0
        if(len(s)==len(t)):
            for i in range(len(s)):
                if(s[i]==t[i]):
                    count+=1
            if(count==len(s)):
                return True
            else:
                return False
        else:
            return False
            
        