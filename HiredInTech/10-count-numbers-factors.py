import math

def count_numbers_factors_my(n):
    # Write your code here
    # First find all prime factors of n, say p1, p2..pi
    # Suppose the number of p1 as factors in n is g1, 
    # the number of factors will be (g1+1) * (g2+1) * ... * (gi + 1)
    # eg: 36 = 2 * 2 * 3 * 3, 
    # p1 = 2, p2 = 3, g1 = 2, g2 = 2
    # the number of factors is ( 2 + 1) * ( 2 + 1) = 9
    # 1, 2, 3, 4, 6, 9, 12, 18, 36

    isPrime = [True] * (n + 1)

    num = 1
    for i in range(2, n + 1):
        if isPrime[i]:
            if n % i == 0:
                cnt = 0
                m = n
                while m % i == 0:
                    m = m / i
                    cnt += 1
                num *= (cnt + 1)

            j = i * i
            while j <= n:
                isPrime[j] = False
                j += i

    return num

# optimized version:
# Only iterate to sqrt(n): if n becomes 1 after the for loop,
# it means all the prime factors are found and all prime factors <= sqrt(n).
# If n > 1, it means there is one (and only one) prime factor that is >= sqrt(n),
# so we need to multiply the number of factors found below sqrt(n) by 2
def count_numbers_factors_op(n):
    # Write your code here

    limit = int(math.sqrt(n))
    isPrime = [True] * (limit + 1)
    

    num = 1
    for i in range(2, limit + 1):
        if isPrime[i]:
            cnt = 0
            while n % i == 0:
                n = n / i
                cnt += 1
            num *= (cnt + 1)

            j = i * i
            while j <= limit:
                isPrime[j] = False
                j += i

    if n > 1:
        num *= 2

    return num

print count_numbers_factors_my(2)

