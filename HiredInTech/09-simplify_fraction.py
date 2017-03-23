def simplify_fraction(numerator, denominator, result):
    # Write your code here
    # result[0] = ...
    # result[1] = ...
    x, y = max(numerator, denominator), min(numerator, denominator)

    # finding the greated common divisor, which will be x after the while loop
    while y != 0:
    	x, y = y, x % y

    result[0] = numerator/x
    result[1] = denominator/x


result = [0, 0]

simplify_fraction(77, 22, result)
print result


