#key points: split words: what counts for a word, hyphen? other punctuation?
#how to deal with capitalized word: 

def word_counts(string):
	dict_counts = {}

	start = 0
	while start < len(string):
		word, start = find_word(string, start)

		if word:
			add_word_to_dict(word, dict_counts)

	return dict_counts

#return the word found at 'start' position, also return the next start position
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def find_word(string, start):
	while start < len(string) and string[start] not in alpha:
		start += 1

	end = start
	while end < len(string) and (string[end] in alpha or (
		string[end] == '-' and string[end+1] in alpha)):
		end += 1

	return (string[start:end], end)

#if all the appearances of one word are capitalized, we use the capitalized word as the key.
#Otherwise, use the lowercase word as the key, even if it has some capitalized appearances
def add_word_to_dict(word, dict_counts):
	if word in dict_counts:
		dict_counts[word] += 1

	elif word.lower() in dict_counts:
		dict_counts[word.lower()] += 1

	elif word.capitalize() in dict_counts:
		count = dict_counts[word.capitalize()] + 1
		dict_counts[word] = count
		del dict_counts[word.capitalize()]

	else:
		dict_counts[word] = 1


sentence = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake. The bill came to five dollars."
print word_counts(sentence)





