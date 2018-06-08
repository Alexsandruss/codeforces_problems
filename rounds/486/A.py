# Conditions - https://codeforces.com/contest/988/problem/A
n, k = [int(el) for el in input().split()]
a_list = [int(el) for el in input().split()]
a_set = set(a_list)
if len(a_set) < k:
    print("NO")
else:
    print("YES")
    for j in range(k):
        rate = a_set.pop()
        for i, ai in enumerate(a_list):
            if rate == ai:
                print(i+1, end=" ")
                break
# all tests passed - https://codeforces.com/contest/988/submission/38926862
