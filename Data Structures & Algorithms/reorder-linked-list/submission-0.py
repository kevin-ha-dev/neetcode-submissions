# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head

        # use fast and slow pointer to seperate list in half

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second_half: Optional[ListNode] = slow.next
        slow.next = None
        prev: Optional[ListNode] = None
    

        # reverse second half of the list 

        while second_half: 
            temp: Optional[ListNode] = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp

        
        # merge left and right list together [1, n-1, 2, n-2, 3, n-3]

        left: Optional[ListNode] = head
        right: Optional[ListNode] = prev
        
        while right:
            # save next positions
            left_next: Optional[ListNode] = left.next
            right_next: Optional[ListNode] = right.next
        
            # reconnect
            left.next = right
            right.next = left_next

            # move forward
            left = left_next
            right = right_next

        return None

        

            


        