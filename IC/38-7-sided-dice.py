import random

def rand5():
	return random.randrange(1, 6)

def rand7():
	diced = 27 # an arbitual number which is > 21

	while diced > 21:
		dice1 = rand5()
		dice2 = rand5()
		diced = (dice1 - 1) * 5 + dice2

	return diced % 7 + 1

print rand7()
print rand7()
print rand7()
print rand7()
print rand7()
print rand7()