# Conditions - http://codeforces.com/contest/977/problem/B
n = int(input())
line = input()
doublegrams = {}
for i in range(n-1):
    if line[i:i+2] not in doublegrams.keys():
        doublegrams.update({line[i:i+2]: 1})
    else:
        doublegrams[line[i:i+2]] += 1
max_n = 0
max_key = ""
for key in doublegrams.keys():
    if doublegrams[key] > max_n:
        max_n = doublegrams[key]
        max_key = key
print(max_key)
# All tests passed (78 ms/ 7888 KB) - http://codeforces.com/contest/977/submission/38110920
