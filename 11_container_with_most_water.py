class Solution:
    def maxArea(self, height: List[int]):
        def get_water(left,right):
            return (right-left)*min(height[left],height[right])
        left,right=0,len(height)-1
        maxx=0
        
        while left < right:
            maxx=max(maxx,get_water(left,right))
            if height[left] < height[right]:
                left+=1
            elif height[right] < height[left]:
                right-=1
            elif height[left+1] < height[right-1] and left+1 < right-1:
                right-=1
            else:
                left+=1
        return maxx