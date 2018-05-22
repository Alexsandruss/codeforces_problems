# Conditions - http://codeforces.com/contest/877/problem/C
import math
n = int(input())
print(n+math.floor(n/2))
for even in [True, False, True]:
    for i in range(n):
        if (i+1) % 2 == 1 and not even:
            print(i+1, end=" ")
        if (i+1) % 2 == 0 and even:
            print(i+1, end=" ")
# (PyPy 3) all tests passed - http://codeforces.com/contest/877/submission/38544408
