# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # General strategy is to create two pointers p1 and p2
        # We create a new list using dummy to append the result 
        # We use total % 10 for the sum
        # total // 10 to carry over the 1
        
        p1: Optional[ListNode] = l1
        p2: Optional[ListNode] = l2

        dummy: ListNode = ListNode(0)
        curr: ListNode = dummy

        val1: int = 0
        val2: int = 0
        total: int = 0
        carry: int = 0
        digit: int = 0

        while p1 or p2:
            if p1:
                val1 = p1.val
            else:
                val1 = 0
            if p2:
                val2 = p2.val
            else: 
                val2 = 0
            
            total = val1 + val2 + carry

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

            
            digit = total % 10
            carry = total // 10

            curr.next = ListNode(digit)
            curr = curr.next
        
        if carry: 
            curr.next = ListNode(carry)
        
        return dummy.next


            
