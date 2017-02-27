class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)

        if (n + m) % 2 == 1:
        	median = self.findKthSortedArrays(nums1, nums2, (n+m)//2 + 1)
        else:
        	median = ( self.findKthSortedArrays(nums1, nums2, (n+m)//2) +
        		self.findKthSortedArrays(nums1, nums2, (n+m)//2 + 1) ) * 0.5

        return median

    def findKthSortedArrays(self, nums1, nums2, k):
        print "k: ", k
    	n = len(nums1)
    	m = len(nums2)

        if n + m < k:
            return None

    	if n < m:
    		return self.findKthSortedArrays(nums2, nums1, k)

        if m == 0:
            return nums1[k-1]

        """ h is 1 off the max index of nums2 because when the search end,
        h is the first number in nums2 that does not belong to the first k
        numbers. If all numbers in nums2 belongs to first k, then h stays
        as m.
        """
        l, h = 0, m 
        while l < h:
            # mid is the guess of the first number in nums2 that does not 
            # belong to the first k numbers. So among the first k numbers,
            # nums2 has mid (index: 0 to mid - 1) numbers and 
            # nums1 has k-mid numbers (index: 0 to k-mid-1)
            mid = l + (h - l)//2
            print "mid: ", mid

            # wanting too many from nums1
            if k - mid > n:
                l = mid + 1
            # wanting too many from nums2
            elif k - mid <=0:
                h = mid
            elif nums2[mid] >= nums1[k-mid-1]:
                h = mid
            else:
                l = mid + 1

        index2 = l - 1
        index1 = k - l -1

        max2 = float("-inf") if index2 < 0 else nums2[index2]
        max1 = float("-inf") if index1 < 0 else nums1[index1]

        return max(max2, max1)


a = [1, 2]
b = [3, 4]

c = [1, 3]
d = [2]

print Solution().findMedianSortedArrays(a, b)



    	

