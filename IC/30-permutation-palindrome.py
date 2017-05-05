""" We can also use a set of chars. When the char is met the first time, add it the set,
when it's met the second time, remove it from the set, and so on. There should be no more
than 1 char left in the set at the end if the string can form a palindrome.
"""

def has_palindrom_permutation(s):
	appear_even = {}
	for c in s:
		if c in appear_even:
			appear_even[c] = not appear_even[c]
		else:
			appear_even[c] = False

	num_odd = 0
	# how to iterate a dict: dict.items(), dict.iteritems(), dict.iterkeys(), dict.itervalues()
	for is_even in appear_even.itervalues():
		if not is_even:
			num_odd += 1

	return not (num_odd > 1)

print has_palindrom_permutation('civic')
print has_palindrom_permutation('cciiv')
print has_palindrom_permutation('civc')