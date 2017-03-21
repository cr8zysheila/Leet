'''
a[1] + a[2] + ... + a[i] + (a[2] - a[1]) + (a[3] - a[2]) + (a[i] - a[i-1])
=sum(a[1] ...a[i]) + (a[i] - a[1])
= 2*a[i] - a[1]

greedy doesn't work:
eg: [1, 7, 8, 9, 10, 11]
2*10 -1 > 2*11 - 7
'''

def maximum_completed_tasks(n, t, task_difficulties):
    # Write your code here
    task_difficulties.sort()
    if len(task_difficulties) < 1 or task_difficulties[0] > t:
    	return 0

    summ = task_difficulties[0]
    start = 0
    num = 1
    for i in range(1, len(task_difficulties)):
    	summ += task_difficulties[i]
    	if summ <= t:
    		num += 1
    	else:
    		summ = summ + task_difficulties[start] - task_difficulties[start + 1]
    		start += 1


    return num
    		
tasks = [24, 23, 22, 10, 20]
print maximum_completed_tasks(5, 65, tasks)

