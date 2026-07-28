# Last updated: 7/27/2026, 9:24:10 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        visited = set()
10        curr = head
11
12        while curr:
13            if curr in visited:
14                return True
15            visited.add(curr)
16            curr = curr.next
17        return False