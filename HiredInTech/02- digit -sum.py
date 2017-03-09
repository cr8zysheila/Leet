def digit_sum(number):
    # Write your code here
    
    sm = number % 10 if number >= 0 else number %(-10)
    number = number // 10 if number >= 0 else number // (-10)
    sm = abs(sm)
    number = abs(number)
    
    while number > 0:
        sm += number % 10
        number = number // 10
        
    return sm

print digit_sum(-123)