"""counting from opening paranthesis
"""
def get_closing_parenthesis(sentence, opening):
	count = 0
	
	if sentence[opening] != '(':
		raise Exception("wrong input")

	for i in range(opening, len(sentence)):
		if sentence[i] == '(':
			count += 1

		elif sentence[i] == ')':
			count -= 1
			if count == 0:
				return i 

	return None


"""Counting from the start. We actually don't need to do this.
def get_closing_parenthesis(sentence, opening):
	count = 0
	num_before = 0
	if sentence[opening] != '(':
		raise Exception("wrong input")

	for i in range(0, len(sentence)):
		if sentence[i] == '(':
			count += 1
			if i == opening:
				num_before = count - 1

		elif sentence[i] == ')':
			count -= 1
			if i > opening and count == num_before:
				return i 

		if count < 0:
			return None
	return None
"""

		
sent = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing"
print get_closing_parenthesis(sent, 10)
	 
