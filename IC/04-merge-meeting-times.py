
#http://yucoding.blogspot.com/search/label/leetcode

# can the merge part be done with divide and conquer? NO NO NO

# Compare with the skyline problem:
# https://briangordon.github.io/2014/08/the-skyline-problem.html


intervals = [(2, 6), (1, 8), (3, 5), (7, 9)]

def merge_meeting_times(intervals):
	if len(intervals) <= 1:
		return intervals

	intervals.sort(key = lambda x: x[0])

	result = [intervals[0]]
	for i in range(1, len(intervals)):
		#last_merged = result[len(result) - 1]
		last_merged = result[-1]

		if last_merged[1] >= intervals[i][0]:
			new_interval = (last_merged[0], 
				max(last_merged[1], intervals[i][1]))
			result.pop()
			result.append(new_interval)
			#the following doesn't work for tuple, will work if it's list
			#result[-1][1] = max(last_merged[1], intervals[i][1])
		else:
			result.append(intervals[i])

	return result

# trying to solve it using divide and conquer:
# IT DOES NOT WORK!!!!!
def merge_meeting_times_DC(intervals):
	if len(intervals) <= 1:
		return intervals

	intervals.sort(key = lambda x: x[0])

	mid = len(intervals) // 2

	left_half = merge_meeting_times_DC(intervals[0: mid])
	print "left_half:", left_half
	right_half = merge_meeting_times_DC(intervals[mid: len(intervals)])
	print "right_half:", right_half

	last_left = left_half[-1]
	first_right = right_half[0]

	# Only check last_left with first_right is not enough:
	# eg: left: [(1, 8)], right[(3, 5), (7, 9)]
	# THE FOLLOWING WILL NOT WORK!!!!!
	# Also, it takes the same number of testing for merges as 
	# the liner method above, since all intervals need to be 
	# tested for merge once
	if last_left[1] >= first_right[0]:
		new_interval = (last_left[0], 
			max(last_left[1], first_right[1]))
		left_half.pop()
		left_half.append(new_interval)
		left_half.extend(right_half[1:])
	else:
		left_half.extend(right_half)

	print "left_half after merge:", left_half

	return left_half



print merge_meeting_times(intervals)
