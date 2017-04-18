def highest_product_of_3(nums):
    if len(nums) < 3:
        raise Exception("Array has less than three numbers")

    ''' the following statement is wrong. If nums[0] happens to be
    the maxi, then we won't find the real second and third maxi. If 
    nums[0] happens to be the mini, then we won't find the real 
    second mini
    '''
    #mini, second_mini, maxi, second_maxi, third_maxi = [nums[0]] * 5
    third_maxi, second_maxi, maxi = nums[0], nums[1], nums[2]
    if third_maxi > second_maxi:
        third_maxi, second_maxi = second_maxi, third_maxi
    if second_maxi > maxi:
        second_maxi, maxi = maxi, second_maxi
    if third_maxi > second_maxi:
        third_maxi, second_maxi = second_maxi, third_maxi

    mini, second_mini = third_maxi, second_maxi

    for i in range(3, len(nums)):
        if nums[i] > maxi:
            maxi, second_maxi, third_maxi = nums[i], maxi, second_maxi
        elif nums[i] > second_maxi:
            second_maxi, third_maxi = nums[i], second_maxi
        elif nums[i] > third_maxi:
            third_maxi = nums[i]
        elif nums[i] < mini:
            mini, second_mini = nums[i], mini
        elif nums[i] < second_mini:
            second_mini = nums[i]
        else:
            pass

    return max(maxi * second_maxi * third_maxi, maxi * mini * second_mini)


nums = [1, 10, -5, 1, -100]
#nums = [-1, -2, -3]
print highest_product_of_3(nums)



'''
1. What if we wanted the highest product of 4 items?
2. What if we wanted the highest product of k items?

.Find the highest k numbers(high[]) and the lowest k numbers(low[])
    with priority queue(heapq) and keep the numbers in increasing order
.if high[k-1]*high[k-2] > low[0] * low[1]
    result *= high[k-1]*high[k-2]
    move index to high down, next to compare
    high[k-3]*high[k-4] with low[0] * low[1]

 else
    result * = low[0] * low[1]
    move index to low up, next to compare
    high[k-1] * high[k-2] with low[2]*low[3]
.loop the above till we got k items for the product
'''