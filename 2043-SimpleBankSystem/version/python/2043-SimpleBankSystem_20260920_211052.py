# Last updated: 9/20/2026, 9:10:52 PM
1class Bank:
2
3    def __init__(self, balance: list[int]):
4        self.balance = balance
5        self.n = len(self.balance)
6
7    def transfer(self, account1: int, account2: int, money: int) -> bool:
8        if account1 > self.n or account2 > self.n or money > self.balance[account1 - 1]:
9            return False
10        else:
11            self.balance[account1 - 1] -= money
12            self.balance[account2 - 1] += money
13            return True
14
15
16    def deposit(self, account: int, money: int) -> bool:
17        if account > self.n:
18            return False
19        else:
20            self.balance[account - 1] += money
21            return True
22
23    def withdraw(self, account: int, money: int) -> bool:
24        if account > self.n or money > self.balance[account - 1]:
25            return False
26        else:
27            self.balance[account - 1] -= money
28            return True
29
30
31# Your Bank object will be instantiated and called as such:
32# obj = Bank(balance)
33# param_1 = obj.transfer(account1,account2,money)
34# param_2 = obj.deposit(account,money)
35# param_3 = obj.withdraw(account,money)