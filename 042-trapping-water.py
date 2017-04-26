class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        level = 0
        total = 0

        while left < right:
        	low = min(height[left], height[right])
        	level = max(level, low)

        	if level > low:
        		total += level - low
        	if height[left] < height[right]:
        		left += 1
        	else:
        		right -= 1


        return total
