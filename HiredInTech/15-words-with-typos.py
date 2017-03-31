def count_words_with_typos(text, target):
	wordList = processed(text)
	print text
	print wordList
	target = target.lower()
	count = 0
	for word in wordList:
		if len(word) == len(target) and diff_2_letters(word, target):
			count += 1
		elif abs(len(word) - len(target)) == 1:
			if add_remove_1(word, target):
				count += 1

	return count

def processed(text):
	wordList = []
	word = []
	for c in text:
		if c.isalnum():
			word.append(c.lower())
		elif word:
			wordList.append("".join(word))
			del word[:]
		else:
			pass
	if word:
		wordList.append("".join(word))

	return wordList

def diff_2_letters(word, target):
	if len(word) != len(target):
		return False

	diffs = 0
	for i in range(0, len(word)):
		if word[i] != target[i]:
			diffs += 1
			if diffs > 2:
				return False

	return True


def add_remove_1(word, target):
	print word
	if abs(len(word) - len(target)) != 1:
		return False

	shorter = min(word, target, key = lambda s: len(s))
	longer = max(word, target, key = lambda s: len(s))

	i, j = 0, 0
	diffs = 0
	while i < len(shorter) and j < len(longer):
		if shorter[i] != longer[j]:
			j += 1
			diffs += 1
			if diffs > 1:
				return False
		else:
			j += 1
			i += 1

	return True

target = "banana"
text = "there are three bananas on the tree and one banano on the ground banonoa banan"

print count_words_with_typos(text, target)





 