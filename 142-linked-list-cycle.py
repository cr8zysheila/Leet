class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None



class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    if not head or not head.next:
    	#raise Exception('Linked list has less than two nodes')
    	return None

    slow, fast = head.next, head.next.next

    while slow and fast and fast.next and slow != fast:
    	slow = slow.next
    	fast = fast.next.next

    # no cycle
    if slow != fast:
    	return None

    # has the cycle, find the entrance of the circle. See Leet 287
    slow = head
    while slow != fast:
    	slow = slow.next
    	fast = fast.next

    return slow




