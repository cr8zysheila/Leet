import random
def rand7():
	return random.randrange(1, 8)

def rand5():
	result = rand7()
	while result > 5:
		result = rand7()

	return result


print rand5()
print rand5()
print rand5()
print rand5()
print rand5()
print rand5()
