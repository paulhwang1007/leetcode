# Last updated: 8/10/2026, 5:33:04 PM
1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.minStack = []
6
7    def push(self, value: int) -> None:
8        self.stack.append(value)
9
10        if len(self.minStack) == 0 or self.minStack[-1] >= value:
11            self.minStack.append(value)
12
13    def pop(self) -> None:
14        if self.stack[-1] == self.minStack[-1]:
15            self.minStack.pop()
16        self.stack.pop()
17
18    def top(self) -> int:
19        return self.stack[-1]
20
21    def getMin(self) -> int:
22        return self.minStack[-1]
23
24
25# Your MinStack object will be instantiated and called as such:
26# obj = MinStack()
27# obj.push(value)
28# obj.pop()
29# param_3 = obj.top()
30# param_4 = obj.getMin()