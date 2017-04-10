from collections import deque
def net_connections(num_nodes, edges, id):
	node_edges = [[] for i in range(0, num_nodes)]
	node_visited = [False for i in range(0, num_nodes)]

	for edge in edges:
		start, end = edge
		node_edges[start - 1].append(end - 1)
		node_edges[end - 1].append(start - 1)

	print node_edges
	print node_visited
	#BFS: check visited both when enqueue and when dequeue

	queue = deque()
	queue.append(id - 1)
	counter = 0
	while queue:
		current = queue.popleft()
		#check visited when dequeue, because the same node may be enqueued more than once
		if node_visited[current] == False:
			counter += 1
			node_visited[current] = True
		for node in node_edges[current]:
			if node_visited[node] == False:
				queue.append(node)

	return  counter - 1

num_nodes = 7
edges = ((1, 2), (1, 4), (4, 2), (4, 3), 
	(3, 1), (5, 6), (5, 7), (7, 6))

print net_connections(7, edges, 2)

