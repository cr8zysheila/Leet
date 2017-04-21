denominations = [1, 2, 3]

''' This solution will produce wrong answer because it counts
same set of coins multiple times. eg:
when computing for ways[3]:
pick up from ways[0]: (0, 3)
pick up from ways[1]: (0, 1, 2)
pick up from ways[2]: (0, 2, 1), (1, 1, 1)
(0, 1, 2) and (0, 2, 1) are duplicate
''''''
def ways_makings_change(amount, denominations):
	ways = [0] * (amount + 1)

	ways[0] = 1
	for i in range(1, len(ways)):
		n = 0
		for coin in denominations:
			if i - coin >= 0:
				n += ways[i-coin]

		ways[i] = n

	print ways
	return ways[-1]
'''

'''
To avoid the problem of the above solution, we loop through the 
denominations first. It's like to force the order of choosing coins
first only use coins of 1, then add coins of 2, then coins of 3...
so the duplicates are avoided
'''
def ways_makings_change(amount, denominations):
	ways = [0] * (amount + 1)
	ways[0] = 1
	for coin in denominations:
		for i in range(coin, len(ways)):
			ways[i] += ways[i - coin]

	return ways[-1]
print ways_makings_change(4, denominations)