def recursive_permutation(s):
	if len(s) <= 1:
		return s

	s_1 = s[0:len(s) - 1]
	perm_set_s_1 = recursive_permutation(s_1)

	result = []
	for i in range(0, len(perm_set_s_1)):
		for j in range(0, len(s_1)):
			new_perm = perm_set_s_1[i][0:j] + s[len(s) - 1] + perm_set_s_1[i][j: len(s_1)]
			result.append(new_perm)
		result.append(perm_set_s_1[i] + s[len(s) - 1])

	return result



print recursive_permutation('cat')

