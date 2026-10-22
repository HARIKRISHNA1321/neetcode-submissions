class Solution:
    def isPalindrome(self, s: str) -> bool:

        s=s.lower()
        s1=""
        for x in s:
            if x.isalnum():
                s1+=x

        if s1==s1[::-1]:
            return True
        else:
            return False

        

        