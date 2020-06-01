# https://codeforces.com/problemset/problem/282/A
# Verdict: Accepted
# Time: 109 ms
# Memory: 16KB
# CbyM

x = 1
total = 0
n = int(input())
for i in range(n):
    user = input()
    if user == '++X' or user == 'X++':
        total += 1
    else:
        total -= 1
print(total)