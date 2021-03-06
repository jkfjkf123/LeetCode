# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        p = head
        while l1 and l2:
            if l1.val > l2.val:
                p.next = l2
                l2 = l2.next
                p = p.next
            else:
                p.next = l1
                l1 = l1.next
                p = p.next
        if l1:
            p.next = l1
        else:
            p.next = l2
        return head.next

