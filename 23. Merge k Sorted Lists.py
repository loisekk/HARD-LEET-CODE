# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        new_list = []
        for p in lists:
            while p :
                new_list.append(p.val)
                p =p.next

            
        fake = ListNode(0)
        current = fake
        for val in sorted(new_list):
            current.next = ListNode(val)
            current = current.next
        return fake.next