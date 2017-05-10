def merge_array(list1, list2):
	result = []

	total_len = len(list1) + len(list2)
	i1, i2 = 0, 0

	while len(result) < total_len:
		#the key point here is to keep it DRY( don't repeat yourself)
		if i1 < len(list1) and ( i2 >= len(list2) or list1[i1] < list2[i2]):
			result.append(list1[i1])
			i1 += 1

		else:
			result.append(list2[i2])
			i2 += 1

	return result


his_list = [3, 4, 6, 10, 11, 15]
her_list = [1, 5, 8, 12, 14, 19]

print merge_array(his_list, her_list)