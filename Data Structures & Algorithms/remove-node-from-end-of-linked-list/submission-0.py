# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we are going to use slow and fast pointers 
        # fast will move up n nodes 
        # slow will start on dummy node bc we want it one node before target
        # slow.next = slow.next.next changes the pointers 
        # we return dummy.next

        dummy: ListNode = ListNode(0, head)

        fast: Optional[ListNode] = head
        slow: Optional[ListNode] = dummy

        for i in range(n):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next
        