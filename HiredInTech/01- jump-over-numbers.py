def jump_over_numbers(list):
    # Write your solution here

    # No solution return -1: emtpy list, value 0

    
    if len(list) < 1:
        return -1
    
    steps = 0
    index = 0
    while index < len(list):
        if list[index] == 0:
            return -1
        index += list[index]
        steps += 1
        
    return steps

a = [3, 4, 1, 2, 5, 6, 9, 0, 1, 2, 3, 1]
print jump_over_numbers(a)