def two_sum(total, nums):
	appeared = set()
	for num in nums:
		if total - num in appeared:
			return True
		else:
			appeared.add(num)

	return False


nums = [2, 8, 6, 4, 5, 3]

print two_sum(9, nums)
print two_sum(4, nums)
