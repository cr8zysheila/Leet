class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
        	return head

        prev_node, curr_node, next_node = head, head.next, head.next.next
        head.next = None

        while curr_node:
        	curr_node.next = prev_node
        	prev_node = curr_node
        	curr_node = next_node
        	if next_node:
        		next_node = next_node.next

        return prev_node