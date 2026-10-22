class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        s1=""
        for x in s:
            if x.isalnum():
                s1+=x.lower()

        if s1==s1[::-1]:
            return True
        else:
            return False

        

        