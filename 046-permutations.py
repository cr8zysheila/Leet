class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
        	return [nums]

        nums_1 = nums[0:len(nums) - 1]
        perms_nums_1 = self.permute(nums_1)

        result = []
        val = nums[len(nums) - 1] 
        for i in range(0, len(perms_nums_1)):
        	for j in range(0, len(nums_1)):
        		new_perm = perms_nums_1[i][0: j] + [val] + perms_nums_1[i][j: len(nums_1)]
        		result.append(new_perm)
        	result.append(perms_nums_1[i] + [val])

        return result

A = [1, 2, 3]
print Solution().permute(A)