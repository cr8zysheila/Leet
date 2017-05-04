def reverse(string):
	if len(string) <= 1:
		return string

	char_list = list(string)
	l, r = 0, len(char_list) - 1
	print l, r
	while l < r:
		char_list[l], char_list[r] = char_list[r], char_list[l]
		l += 1
		r -= 1

	return ''.join(char_list)


print reverse('abcd')