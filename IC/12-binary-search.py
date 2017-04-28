def binary_search(target, nums):
	if len(nums) < 1:
		return False
	left, right = 0, len(nums) - 1

	while left < right:
		mid = left + (right - left)//2

		if target <= nums[mid]:
			right = mid
		else:
			left = mid + 1

	return target == nums[left]


nums = [2, 3, 4, 6, 7]
nums2 = [1]

print binary_search(2, nums)
print binary_search(7, nums)
print binary_search(6, nums)
print binary_search(1, nums)
print binary_search(5, nums)
print binary_search(8, nums)

print binary_search(1, nums2)
print binary_search(2, nums2)
print binary_search(0, nums2)