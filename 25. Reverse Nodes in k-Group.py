# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dum = ListNode(0)
        dum.next = head
        prev = dum
        while True:
            node = prev
            for i in range(k):
                node = node.next
                if not node:
                    return dum.next
            curr = prev.next
            nxt = node.next

            p_node = nxt
            while curr != nxt:
                    temp =curr.next
                    curr.next = p_node
                    p_node = curr
                    curr = temp
            temp = prev.next
            prev.next = node
            prev = temp
