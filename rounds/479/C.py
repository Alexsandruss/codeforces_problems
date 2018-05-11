# Conditions - http://codeforces.com/contest/977/problem/C
n, k = [int(el) for el in input().split(" ")]
sequence = [int(el) for el in input().split(" ")]
sequence.sort()
result = -1
if n == 1:
    if k == 0:
        result = sequence[0] - 1
    else:
        result = sequence[0]
elif n == k:
    result = sequence[k-1]
else:
    if k == 0:
        result = sequence[0] - 1
    else:
        if sequence[k-1] == sequence[k]:
            result = -1
        else:
            result = sequence[k-1]
if result <= 0 or result > 10**9:
    result = -1
print(result)
# All tests passed (233 ms/22300 KB) - http://codeforces.com/contest/977/submission/38120177
