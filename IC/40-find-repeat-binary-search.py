# use  binary search kinda way to find the repeat. time complexity (nlgn), space (1)

def find_repeat(nums):
	l, h = 0, len(nums) - 1
	while l < h:
		mid = l + ( h - l)//2

		count = 0
		for i in nums:
			if l <= i <= mid:
				count += 1

		if count > (mid - l) + 1:
			h = mid

		else:
			l = mid + 1

	return l

nums = [6, 5, 5, 7, 3, 4, 2, 1]
print find_repeat(nums)
