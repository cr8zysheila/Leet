import math
def all_prime_factors(n):
	# Write your code here
	# Return a list with the prime decomposition numbers

	result = []
	limit = int(math.sqrt(n))
	isPrime = [True] * (limit + 1)

	for i in range(2, limit + 1):
		if isPrime[i]:
			while n % i == 0:
				n = n / i
				result.append(i)

			j = i * i
			while j <= limit:
				isPrime[j] = False
				j += i

	# one more prime factor left, which is > sqrt(n)
	if n > 1:
		result.append(n)

	return result


print all_prime_factors(9901)



