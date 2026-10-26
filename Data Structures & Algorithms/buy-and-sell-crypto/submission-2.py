class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        profit=0
        minimum=prices[i]
        

        
        while i<len(prices) :
            if minimum>prices[i]:
                minimum=prices[i]
                
            x=prices[i]-minimum
            if x>profit:
                profit=x
            
            
            i+=1
        
        return profit

        
        
        

        