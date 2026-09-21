# Last updated: 9/20/2026, 9:17:50 PM
1class Bank:
2
3    def __init__(self, balance: list[int]):
4        self.balance = balance
5        self.n = len(balance)
6
7    def _valid_account(self, account: int) -> bool:
8        return 1 <= account <= self.n
9
10    def transfer(self, account1: int, account2: int, money: int) -> bool:
11        if not self._valid_account(account1) or not self._valid_account(account2):
12            return False
13        if money > self.balance[account1 - 1]:
14            return False
15    
16        self.balance[account1 - 1] -= money
17        self.balance[account2 - 1] += money
18        return True
19
20
21    def deposit(self, account: int, money: int) -> bool:
22        if not self._valid_account(account):
23            return False
24
25        self.balance[account - 1] += money
26        return True
27
28    def withdraw(self, account: int, money: int) -> bool:
29        if not self._valid_account(account):
30            return False
31        if money > self.balance[account - 1]:
32            return False
33
34        self.balance[account - 1] -= money
35        return True
36
37
38# Your Bank object will be instantiated and called as such:
39# obj = Bank(balance)
40# param_1 = obj.transfer(account1,account2,money)
41# param_2 = obj.deposit(account,money)
42# param_3 = obj.withdraw(account,money)