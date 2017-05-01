# similar to Leet 136: single number
class Solution(object):
    def missingNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums)
        for i in range(0, len(nums)):
            result = result + i - nums[i]

        return result

    def missingNumber_(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums)
        for i in range(0, len(nums)):
            result ^= i
            result ^= nums[i]

        return result