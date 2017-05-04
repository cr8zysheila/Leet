class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #use a dummy node to solve the case when the nth node from end is the head
        dummy = ListNode(0)
        dummy.next = head

        # draw an example to calculate how many nodes to go
        front, end = dummy, dummy
        for i in range(0, n+1):
        	if not end:
        		raise Exception('not enough nodes')
        	end = end.next

        while end:
        	front = front.next
        	end = end.next

        front.next = front.next.next
        return dummy.next

node1 = ListNode(1)
print Solution().removeNthFromEnd(node1, 1)