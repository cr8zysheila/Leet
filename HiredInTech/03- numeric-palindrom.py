def is_numeric_palindrome(n):
    # Write your code here
    if n < 0:
        return False
    
    num = n
    length = 0
    while num > 0:
        length += 1
        num = num // 10
        
    while n >= 10:
        high = n//(10**(length - 1))
        low = n % 10
        if high != low:
            return False
        n = n % (10**(length - 1))
        n = n // 10
        length -= 2

    return True

print is_numeric_palindrome(23)