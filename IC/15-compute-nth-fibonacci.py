def nth_fibonacci(n):
	if n < 0:
		raise Exception("must be positive number")

	if n <= 1:
		return n

	prev1, prev2 = 1, 0 
	fib = 0

	for i in range(2, n+1):
		fib = prev1 + prev2
		prev1, prev2 = fib, prev1

	return fib


print nth_fibonacci(3)
print nth_fibonacci(5)
print nth_fibonacci(6)
