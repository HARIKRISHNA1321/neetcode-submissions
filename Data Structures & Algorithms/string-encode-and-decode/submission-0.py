class Solution:
    def encode(self, strs: List[str]) -> str:
        s=""
        for x in strs:
            s+=str((len(x)))
            s+=("#")
            s+=(x)
        return s

    def fun(self,i,s,l1):
        num=""
        while s[i]!="#":
            num+=(s[i])
            i+=1
        i+=1
        
        num=int(num)
        string=s[i:i+num]
        i=i+num
        l1.append(string)
        return l1,i
    
    def decode(self, s: str) -> List[str]:
        i=0
        l1=[]
        while i!=(len(s)):
            l1,i=self.fun(i,s,l1)
        return l1
        





                 

        
