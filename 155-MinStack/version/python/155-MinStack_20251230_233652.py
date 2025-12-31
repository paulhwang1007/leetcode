# Last updated: 12/30/2025, 11:36:52 PM
1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.minStack = []
6
7    def push(self, val: int) -> None:
8        self.stack.append(val)
9        val = min(val, self.minStack[-1] if self.minStack else val)
10        self.minStack.append(val)
11
12    def pop(self) -> None:
13        self.stack.pop()
14        self.minStack.pop()
15
16    def top(self) -> int:
17        return self.stack[-1]
18
19    def getMin(self) -> int:
20        return self.minStack[-1]
21
22
23# Your MinStack object will be instantiated and called as such:
24# obj = MinStack()
25# obj.push(val)
26# obj.pop()
27# param_3 = obj.top()
28# param_4 = obj.getMin()