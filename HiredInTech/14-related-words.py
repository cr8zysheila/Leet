def most_related_word(text, target, distance):
	wordList = processed(text)
	target = target.lower()

	wordDict = {}
	for i, word in enumerate(wordList):
		if word == target:
			appeared = {target}
			j = i
			step = 1
			count = 0
			while  0 <= j < len(wordList) and count < distance:
				if wordList[j] not in appeared:
					if wordList[j] in wordDict:
						wordDict[wordList[j]] += 1
					else:
						wordDict[wordList[j]] = 1
					appeared.add(wordList[j])
					count += 1
					if count == distance and step == 1:
						count = 0
						j = i
						step = -1
				j += step

	result = ''
	wordDict[result] = 0

	for word, num in wordDict.items():
		if num > wordDict[result]:
			result = word
		elif num == wordDict[result]:
			result = min(result, word)
		else:
			pass

	return result


def processed(text):
	wordList = []

	word = []
	for c in text:
		if c.isalnum():
			word.append(c.lower())
		elif len(word) > 0:
			wordList.append("".join(word))
			del word[:]
		else:
			pass
	# don't forget the last word in the buffer
	if word:
		wordList.append("".join(word))


	return wordList

#text = "We are the 'Rock' Stars!!"
text ='It is a nice day today, the sun is shining. However, the weather is expected to get worse the following few days. Nice day by day weather forecasts can be found literally everywhere on the "Internet". So, it is quite easy to know what to expect tomorrow.'
target = 'day'
distance = 3
#print processed(text)

print most_related_word(text, target, distance)

#text = input()
#target = input()
#distance = input()