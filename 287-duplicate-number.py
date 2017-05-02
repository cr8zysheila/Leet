'''
we do (sum(nums) - sum(1 to n)) to find out the duplicate number if it the duplicate only
appear twice, but it may cause overflow. and it doen't work if the duplicate appears more
than twice

Do the 'loop in a linked list' trick with two pointers. If there's only one number that' s
duplicate, then the duplicate will be found from nums[0]. See 287-duplicate-number.JPG
'''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            raise Exception('need at least two elements')
        
        #slow and fast both start from 0, the next steps will be as follow
        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # now slow and fast are at the same element in the loop. Suppose the 
        # length before the loop is L, the length of the circle is C, and slow
        # and fast are at the Mth element in the circle. ( L + M ) * 2 = L + M + n*C,
        # so L = n*C - M. Draw a picture to avoid the off-1 error.
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


nums = [1,3,4,2,1]

print Solution().findDuplicate(nums)