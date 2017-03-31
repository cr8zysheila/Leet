
# find the string pattern in text. return the index in the text where
# the pattern begins. If the pattern is not found, return -1
def find_pattern(s, p, start, prefix):
	# starting index of p
	j = 0
	for i in range(start, len(s) - len(p) + 1):
		while j > 0 and p[j] != s[i]:
			j = prefix[j]
		if p[j] == s[i]:
			j += 1
			if j == len(p):
				return i - j + 1



def build_prefix(p, prefix):
	#prefix[0], prefix[1] = 0, 0
	for i in range(2, len(prefix)):
		j = prefix[i-1]
		while j > 0 and p[j] != p[i]:
			j = prefix[j]
		if p[j] == p[i]:
			prefix[i] = j + 1
		else:
			prefix[i] = 0

def count_string_occurrences(text, pattern):
	count = 0
	start = 0

	prefix = [0] * len(pattern)
	build_prefix(pattern, prefix)
	print prefix

	while start + len(pattern) <= len(text):
		matched = find_pattern(text, pattern, start, prefix)
		if matched < 0:
			break
		count += 1
		start = matched + 1

	return count


text = input("text:")
pattern = input("pattern:")

print count_string_occurrences(text, pattern)

