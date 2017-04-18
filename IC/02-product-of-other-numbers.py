"""this version use O(n) memory and does not consider corner cases
def product_of_other_numbers(nums):
	product_before = [1] * len(nums)
	product_after = [1] * len(nums)

	for i in range(1, len(nums)):
		product_before[i] = product_before[i-1] * nums[i-1]
		j = len(nums) - 1 - i
		product_after[j] = product_after[j+1] * nums[j+1]

	return [product_before[i] * product_after[i] for i in range(0, len(nums))]
"""

def product_of_other_numbers(nums):
	if len(nums) < 2:
		return 1

	result = [1] * len(nums)

	# first compute the product before i
	for i in range(1, len(nums)):
		result[i] = result[i-1] * nums[i-1]

	# now compute the product after i and multiply it to the
	# product before i
	product_after = 1
	for j in range(len(nums)-1, -1, -1):
		result[j] *= product_after
		product_after *= nums[j]

	return result


#nums = [1, 7, 3, 4]
nums = [2, 4]
print product_of_other_numbers(nums)