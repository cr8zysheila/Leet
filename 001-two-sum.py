class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        """ solution 1 """
        """
        for i in range(0, len(nums)-1):
        	for j in range(i+1, len(nums)):
        		if nums[i] + nums[j] == target:
        			return [i, j]
        """

        """ solution 2: 
        	wrong answer for :
        		Input:[3,3], 6
				Output:null
				Expected:[0,1]
        """
        """
        hsh = {}
        for i in range(0, len(nums)):
        	if nums[i] not in hsh:
        		hsh[nums[i]] = i
        for i in range(0, len(nums)):
        	if hsh.get(target - nums[i], None):
        		return [i, hsh[target - nums[i]]]
        """

        """solution 3"""
        """
        hsh = {}
        for i in range(0, len(nums)):
        	if nums[i] not in hsh:
        		if (target - nums[i]) not in hsh:
        			hsh[target - nums[i]] = i
        	else:
        		return [hsh[nums[i]], i]
        """
        # using enumerate() instead of range() can improve performance a lot
        hsh = {}
        for i, num in enumerate(nums):
        	if num not in hsh:
        		if (target - num) not in hsh:
        			hsh[target - num] = i
        	else:
        		return [hsh[num], i]



        	        
