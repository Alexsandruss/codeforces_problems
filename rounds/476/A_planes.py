# Conditions - http://codeforces.com/contest/965/problem/A
import math
line = input()
k, n, s, p = [int(el) for el in line.split(" ")]
print(math.ceil(math.ceil(n/s)*k/p))
"""
All test passed
Time: 78 ms
Memory: 6876 KB
http://codeforces.com/contest/965/submission/37664968
"""