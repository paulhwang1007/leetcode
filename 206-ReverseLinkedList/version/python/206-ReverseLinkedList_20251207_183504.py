# Last updated: 12/7/2025, 6:35:04 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        prev, curr = None, head
9
10        while curr:
11            next = curr.next # initial pointer
12            curr.next = prev
13            prev = curr
14            curr = next
15        return prev