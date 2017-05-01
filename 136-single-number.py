class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
        	raise Exception('empty list')
        if len(nums) == 1:
        	return nums[0]

        result = 0
        for num in nums:
        	result ^= num

        return result