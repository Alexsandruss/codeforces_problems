# Conditions - http://codeforces.com/contest/919/problem/B
# PyPy
k = int(input())
perfect_number = 10
count = 0
while count < k:
    perfect_number += 9
    if sum([int(el) for el in [symbol for symbol in str(perfect_number)]]) == 10:
        count += 1
print(perfect_number)
# all tests passed - http://codeforces.com/contest/919/submission/38441800
