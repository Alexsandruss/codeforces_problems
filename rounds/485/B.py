# Conditions - https://codeforces.com/contest/987/problem/B
import decimal
decimal.MAX_EMAX = 10**10
decimal.getcontext().Emax = 10**10
x, y = [decimal.Decimal(el) for el in input().split()]
power = decimal.getcontext().power
xy = power(x, y)
yx = power(y, x)
if xy > yx:
    print(">")
elif xy < yx:
    print("<")
else:
    print("=")
