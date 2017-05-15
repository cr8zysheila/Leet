'''
a[1] + a[2] + ... + a[i] + (a[2] - a[1]) + (a[3] - a[2]) + (a[i] - a[i-1])
=sum(a[1] ...a[i]) + (a[i] - a[1])

cost(2, i+1) - cost(2, i) = 2*a[i+1] - a[i]
cost(2, i+1) - cost(1, i) = 2*a[i+1] - a[i] - a[2] > 0

so it has to start from the smallest task
'''

def maximum_completed_tasks(n, t, task_difficulties):
    # Write your code here
    task_difficulties.sort()
    if len(task_difficulties) < 1 or task_difficulties[0] > t:
    	return 0

    summ = task_difficulties[0]
    num = 1
    for i in range(1, len(task_difficulties)):
    	summ += 2*task_difficulties[i] - task_difficulties[i-1]
    	if summ <= t:
    		num += 1
    	else:
    		break


    return num
    		
tasks = [24, 23, 22, 10, 20]
print maximum_completed_tasks(5, 65, tasks)

