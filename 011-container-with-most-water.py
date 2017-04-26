class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        most_water = 0

        # when left < right, all containers made from (left, right -1),
        # (left, right -2)...(left, left) are smaller than container
        # (left, right), so we don't need to check them. Instead, we 
        # continue to check (left+1, right)
        while left < right:
        	water_hold = min(height[left], height[right]) * (right - left)
        	most_water = max(most_water, water_hold)
        	if height[left] < height[right]:
        		left += 1
        	else:
        		right -= 1

        return most_water