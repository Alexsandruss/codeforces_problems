# Conditions - https://codeforces.com/contest/705/problem/A
n = int(input())
result = ""
for i in range(n):
    if i % 2 == 0:
        result += "I hate"
    else:
        result += "I love"
    if i != n-1:
        result += " that "
    else:
        result += " it"
print(result)
# all tests passed - https://codeforces.com/contest/705/submission/38975520
