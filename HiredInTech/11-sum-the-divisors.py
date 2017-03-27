import math

def sum_the_divisors(n):
    # Write your code here
    limit = math.sqrt(n)
    summ = 0
    for i in range(1, int(limit) + 1):
    	if n % i == 0:
    		summ += i
    		print summ
    		if i != limit:
    			summ += n / i
    			print summ


    return summ


print sum_the_divisors(8)