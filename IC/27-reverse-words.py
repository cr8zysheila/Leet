def reverse(char_list, left, right):
	while left < right:
		char_list[left], char_list[right] = char_list[right], char_list[left]
		left += 1
		right -= 1


def reverse_words(string):
	char_list = list(string)

	reverse(char_list, 0, len(char_list) - 1)

	start, end = 0, 0
	while end < len(char_list):
		start = end
		while end < len(char_list) and char_list[end] != ' ':
			end += 1

		reverse(char_list, start, end - 1)

		while end < len(char_list) and char_list[end] == ' ':
			end += 1

	return ''.join(char_list)

print reverse_words('went to see the circus')

