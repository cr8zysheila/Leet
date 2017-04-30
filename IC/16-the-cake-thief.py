def max_duffle_value(capacity, cakes):
	max_value = [0] * (capacity + 1)

	for i in range(0, len(max_value)):
		for weight, value in cakes:
			if weight == 0 and value > 0:
				raise Exception("infinity")
			if weight <= i:
				max_value[i] = max(max_value[i], max_value[i - weight] + value)

	return max_value[-1]


cakes = [(3, 40), (5, 70), [0, 1]]

print max_duffle_value(9, cakes)