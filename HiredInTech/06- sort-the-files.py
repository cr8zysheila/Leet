'''
1
10
100
1000
1001
1002
1003
101
102
 .
 .
 .
109
11
110
 .
 .
 .
199
2
20
200
201
202
 .
 .
 .
209
21
210
 .
 .
 .
299
3
30
300
301
 .
 .
 .
'''
MAX_LEN = 100
def sort_the_files(n, result):
    # Write your solution here
    nums = []
    recursive_gen(n, nums, 1, "")

    for numStr in nums:
    	result.append("IMG" + numStr + ".jpg")


def recursive_gen(n, nums, start, prefix):
	size = min(n, MAX_LEN)
	for i in range(start, 10):
		numStr = prefix + str(i)
		if int(numStr) <= n and len(nums) < size:
			nums.append(numStr)
			recursive_gen(n, nums, 0, numStr)
		else:
			break


result = []
sort_the_files(103, result)
print result
