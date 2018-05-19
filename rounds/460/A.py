# Conditions - http://codeforces.com/contest/919/problem/A
n, m = [int(el) for el in input().split()]
costs = []
for i in range(n):
    a, b = [int(el) for el in input().split()]
    costs.append(a/b)
print(min(costs)*m)
# all tests passed - http://codeforces.com/contest/919/submission/38441225
