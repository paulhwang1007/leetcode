# Last updated: 12/19/2025, 9:26:43 AM
1class Node:
2    def __init__(self, key, val):
3        self.key, self.val = key, val
4        self.prev = self.next = None
5
6class LRUCache:
7
8    def __init__(self, capacity: int):
9        self.cap = capacity
10        self.cache = {} # map key to node
11
12        # Left = LRU, Right = MRU
13        self.left, self.right = Node(0, 0), Node(0, 0)
14        self.left.next, self.right.prev = self.right, self.left
15
16    # remove node from list
17    def remove(self, node):
18        prev, nxt = node.prev, node.next
19        prev.next, nxt.prev = nxt, prev
20
21    # insert at right
22    def insert(self, node):
23        prev, nxt = self.right.prev, self.right
24        prev.next = nxt.prev = node
25        node.next, node.prev = nxt, prev
26
27    def get(self, key: int) -> int:
28        if key in self.cache:
29            self.remove(self.cache[key])
30            self.insert(self.cache[key])
31            return self.cache[key].val
32        return -1
33
34    def put(self, key: int, value: int) -> None:
35        if key in self.cache:
36            self.remove(self.cache[key])
37        self.cache[key] = Node(key, value)
38        self.insert(self.cache[key])
39
40        if len(self.cache) > self.cap:
41            # remove from the list and delete LRU from hashmap
42            lru = self.left.next
43            self.remove(lru)
44            del self.cache[lru.key]
45
46# Your LRUCache object will be instantiated and called as such:
47# obj = LRUCache(capacity)
48# param_1 = obj.get(key)
49# obj.put(key,value)