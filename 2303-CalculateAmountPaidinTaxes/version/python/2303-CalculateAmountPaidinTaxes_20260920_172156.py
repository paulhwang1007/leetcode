# Last updated: 9/20/2026, 5:21:56 PM
1class Solution:
2    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
3        total_tax = 0.0
4        prev_upper = 0
5
6        for upper, percent in brackets:
7            if income <= prev_upper:
8                break
9            
10            taxable_income = min(income, upper) - prev_upper
11            total_tax += taxable_income * (percent / 100)
12            prev_upper = upper
13        
14        return total_tax