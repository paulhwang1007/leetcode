# Last updated: 9/20/2026, 4:58:31 PM
1class Solution:
2    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
3        income_left = income
4        total_tax = 0
5
6        for i in range(len(brackets)):
7            if i != 0:
8                taxable_income = brackets[i][0] - brackets[i-1][0]
9            else:
10                taxable_income = brackets[i][0]
11
12            if income_left >= taxable_income:
13                current_tax = taxable_income * (brackets[i][1] / 100)
14                total_tax += current_tax
15                income_left -= taxable_income
16            else:
17                current_tax = income_left * (brackets[i][1] / 100)
18                total_tax += current_tax
19                break
20
21        return total_tax