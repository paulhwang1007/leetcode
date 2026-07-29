# Last updated: 7/29/2026, 12:05:04 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        """
9        Do not return anything, modify head in-place instead.
10        """
11        # find the midpoint of the list
12        slow, fast = head, head.next
13
14        while fast and fast.next:
15            slow = slow.next
16            fast = fast.next.next
17
18        # reverse the second half
19        second = slow.next
20        prev = None
21        slow.next = None
22        while second:
23            next_node = second.next
24            second.next = prev
25            prev = second
26            second = next_node
27
28        # merge the lists
29        first, second = head, prev
30        while second:
31            next_1, next_2 = first.next, second.next
32            first.next = second
33            second.next = next_1
34            first, second = next_1, next_2