class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l , r = 0 , len(heights) - 1
        leftMax , rightMax = heights[l], heights[r]
        print(l,r,leftMax,rightMax)
        while l < r:
            maxArea = max(maxArea, min(heights[l], heights[r]) * (r - l))
            print(maxArea)
            if leftMax < rightMax:
                
                l += 1
                leftMax=max(heights[l], leftMax)
            else:
                
                r -= 1
                rightMax= max(heights[r],rightMax)
        return maxArea

        
