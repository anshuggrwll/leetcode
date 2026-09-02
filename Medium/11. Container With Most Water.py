from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right=len(height)-1
        max_Area=0
        while right>left:
            max_Area=max(max_Area, min(height[right], height[left])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_Area

            

        