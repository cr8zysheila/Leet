# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
class Solution(object):
    def addNode(self, value, l):
        l.next = ListNode(0)
        l = l.next
        l.val = value
        return l

    def addTwoNumbers(self, l1, l2):
        '''
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        '''
        result = ListNode(0)
        l3 = result
        carry = 0
        while l1 != None and l2 != None:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            digit = sum % 10

            l3 = self.addNode(digit, l3)
            l1 = l1.next
            l2 = l2.next

        if l1 != None or l2 != None:
            last = l1 if l1 != None else l2

            while last != None:
                sum = last.val + carry
                carry = sum // 10
                digit = sum % 10

                l3 = self.addNode(digit, l3)
               
                print last.val
                last = last.next


        if carry:
            l3 = self.addNode(carry, l3)
           
        return result.next
"""       

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        l3 = dummy
        carry = 0
        while l1 != None or l2 != None:
            sum = carry
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next

            carry = sum // 10
            digit = sum % 10

            l3.next = ListNode(0)
            l3 = l3.next
            l3.val = digit

        if carry:
            l3.next = ListNode(1)
           
        return dummy.next

L1 = ListNode(1)
L1.next = ListNode(8)

L2 = ListNode(0)

s = Solution()
s.addTwoNumbers(L1, L2)