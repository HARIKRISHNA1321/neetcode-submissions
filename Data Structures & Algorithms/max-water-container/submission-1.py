class Solution:
    def maxArea(self, heights: List[int]) -> int:
        x=0
        i=len(heights)-1
        area=0
        while i>x:
            if (i-x)*min(heights[i],heights[x])>area:
                area=(i-x)*min(heights[i],heights[x])
            if heights[x]<heights[i]:
                x+=1
            else:
                i-=1
        return area


        
        