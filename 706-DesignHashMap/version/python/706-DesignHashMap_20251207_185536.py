# Last updated: 12/7/2025, 6:55:36 PM
1class MyHashMap:
2
3    def __init__(self):
4        self.map = {}
5
6    def put(self, key: int, value: int) -> None:
7            self.map[key] = value
8
9    def get(self, key: int) -> int:
10        if key in self.map:
11            return self.map[key]
12        else:
13            return -1
14
15    def remove(self, key: int) -> None:
16        if key in self.map:
17            self.map.pop(key)   
18
19
20# Your MyHashMap object will be instantiated and called as such:
21# obj = MyHashMap()
22# obj.put(key,value)
23# param_2 = obj.get(key)
24# obj.remove(key)