class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if n <= m:
        	return head

        start = head
        for i in range(1, m):
        	if not start:
        		raise Exception('not enough nodes')
        	start = start.next
        	i += 1

        #start is now the last node that won't reverse
        if not start or not start.next or not start.next.next:
        	raise Exception('not enouth nodes')

        rev_head = start.next
        prev_node, curr_node, next_node = rev_head, rev_head.next, rev_head.next.next

        for i in range(m, n):
        	if not curr_node:
        		raise Exception('not enouth nodes')
        	curr_node.next = prev_node
        	prev_node = curr_node
        	curr_node = next_node
        	if next_node:
        		next_node = next_node.next

        start.next = prev_node
        rev_head.next = curr_node

