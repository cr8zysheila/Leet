def is_single_riffle(half1, half2, shuffled):
	h1, h2 = 0, 0
	for i in range(0, len(shuffled)):
		if h1 < len(half1) and shuffled[i] == half1[h1]:
			h1 += 1
		elif h2< len(half2) and shuffled[i] == half2[h2]:
			h2 += 1
		else:
			return False

	return True


half1 = [1, 2, 3]
half2 = [4, 5, 6]
shuffled1 = [1, 4, 2, 3, 5, 6]
shuffled2 = [1, 4, 6, 5, 2, 3]

print is_single_riffle(half1, half2, shuffled1)
print is_single_riffle(half1, half2, shuffled2)