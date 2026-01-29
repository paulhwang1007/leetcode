# Last updated: 1/29/2026, 12:28:37 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        
12        level = 0
13        q = deque([root])
14        while q:
15            for i in range(len(q)):
16                node = q.popleft()
17                if node.left:
18                    q.append(node.left)
19                if node.right:
20                    q.append(node.right)
21            level += 1
22        return level