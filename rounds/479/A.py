# Conditions - http://codeforces.com/contest/977/problem/A
n, k = [int(el) for el in input().split(" ")]
for i in range(k):
    if str(n).endswith("0"):
        n = round(n / 10)
    else:
        n -= 1
print(n)
# All tests passed (77 ms/7600 KB) - http://codeforces.com/contest/977/submission/38110703
