# Last updated: 7/29/2026, 11:27:40 PM
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
11        slow, fast = head, head.next
12
13        # 1. split the list in half
14        while fast and fast.next:
15            slow = slow.next
16            fast = fast.next.next
17
18        # 2. reverse the second half
19        second = slow.next
20        prev = slow.next = None
21        while second:
22            next_node = second.next
23            second.next = prev
24            prev = second
25            second = next_node
26        
27        # 3. reorder the nodes
28        # Keep track of:
29        #       - head: points to the head
30        #       - prev: points to the last node since second is None rn
31        first, second = head, prev
32        while second:
33            first_next, second_next = first.next, second.next
34            first.next = second
35            second.next = first_next
36            first, second = first_next, second_next
37        
38        