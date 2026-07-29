class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maximum_area = 0
        
        while(left<right):
            width = right - left
            height = min(heights[right],heights[left])
            current_area = width * height
            if current_area > maximum_area:
                maximum_area = current_area
            if height == heights[left]:
                left+=1
            elif height == heights[right]:
                right -=1
        return maximum_area