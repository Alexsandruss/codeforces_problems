# Conditions - http://codeforces.com/contest/978/problem/A
n = int(input())
original_arr = [int(el) for el in input().split(" ")]
new_arr = []
original_arr.reverse()
for original_el in original_arr:
    if original_el not in new_arr:
        new_arr.append(original_el)
new_arr.reverse()
print(len(new_arr))
line = ""
for el in new_arr:
    line += str(el) + " "
print(line[:len(line)-1])
# All tests passed (78 ms/6888 KB) - http://codeforces.com/contest/978/submission/38160700
