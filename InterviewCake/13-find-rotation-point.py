def rotation_point(word_list):
	left = 0
	right = len(word_list) - 1

	while left < right:
		mid = left + (right - left) // 2
		if word_list[mid] < word_list[0]:
			right = mid
		else:
			left = mid + 1

	return left

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

print rotation_point(words)
