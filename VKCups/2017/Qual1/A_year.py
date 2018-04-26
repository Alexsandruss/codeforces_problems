# Conditions - http://codeforces.com/contest/769/problem/A
count = int(input())
input_text = input()
input_text = input_text.split(" ")
sum = 0
for elem in input_text:
    sum += int(elem)
print(int(sum/count))
"""
All tests passed
Time: 62 ms
Memory: 5496 KB
http://codeforces.com/contest/769/submission/35602427
"""