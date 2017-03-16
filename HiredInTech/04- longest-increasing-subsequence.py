'''
Solution 1: n**2

empty list: return empty list
oen element list: return one element list
array A of size N: A[i] is the length of the longest increasing
    subsequence ending with A[i]; init to 0
array B of size N: B[i] is the index of previous value of i in the 
    longest increasing subsequence ending with A[i]; init to -1
maxIndex: the index of the ending value of the LIS currently found


def longest_increasing_subsequence(sequence):
    # Write your solution here
    if len(sequence) < 2:
        return sequence

    A = [0] * len(sequence)
    B = [-1] * len(sequence)
    maxIndex = 0

    for i in range(1, len(sequence)):
        for j in range(0, i):
            if sequence[i] > sequence[j]:
                if A[j] + 1 > A[i]:
                    A[i] = A[j] + 1
                    B[i] = j
                    if A[i] > A[maxIndex]:
                        maxIndex = i


    result = []
    i = maxIndex
    while maxIndex >= 0:
        result.append(sequence[maxIndex])
        maxIndex = B[maxIndex]

    result.reverse()

    return result

'''

'''
Q: duplicates?
Solution 2: nlogn
http://stackoverflow.com/questions/6129682/longest-increasing-subsequenceonlogn
https://www.hiredintech.com/classrooms/algorithm-design/lesson/12/task/14/solution

Array A: A[i] is the index to S where S[A[i]] is the smallest  ending value for the LIS
    of size i
Array B: B[i] is the index of previous value before S[i] in S in the LIS
'''
def longest_increasing_subsequence(sequence):
    # Write your solution here
    A = []
    B = [-1] * len(sequence)

    A.append(0)
    for i in range(1, len(sequence)):
        if sequence[i] < sequence[A[0]]:
            A[0] = i
        elif sequence[i] > sequence[A[len(A) - 1]]:
            A.append(i)
            B[i] = A[len(A) - 2]
        else:
            j = find_place(A, sequence, i)
            # S[j] can not be identical to any of existing ending values
            # if so j will be -1 as returned by find_place
            if j > 0:
                A[j] = i
                B[i] = A[j-1]

    result = []
    i = A[len(A) - 1]
    while i >= 0:
        result.append(sequence[i])
        i = B[i]

    result.reverse()

    return result

def find_place(A, s, i):
    l, h = 0, len(A) - 1

    while l < h:
        mid = l + (h - l)//2
        if s[A[mid]] < s[i]:
            l = mid + 1
        else:
            h = mid
    # l is the position found, but if the value in A[l] is equal to the new
    # value, we just ignore the new value
    if s[A[l]] == s[i]:
        return -1
    else:
        return l



a = [16, 3, 5, 19, 10, 14, 12, 0, 15]
print longest_increasing_subsequence(a)








