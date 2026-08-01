# Last updated: 8/1/2026, 1:27:34 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        # 1. split the list in half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse the second half
        second = slow.next
        prev = slow.next = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        
        # 3. reorder the nodes
        # Keep track of:
        #       - head: points to the head
        #       - prev: points to the last node since second is None rn
        first, second = head, prev
        while second:
            first_next, second_next = first.next, second.next
            first.next = second
            second.next = first_next
            first, second = first_next, second_next
        
        