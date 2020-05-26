# https://codeforces.com/problemset/problem/231/A
# Verdict: Accepted
# Memory: 20 KB
# Time: 218 ms
# CbyM

n = int(input())
certainty = 0
for i in range(0, n):
    Petya, Vasya, Tonya = list(map(int, input().split()))
    if Petya + Vasya + Tonya >= 2:
        certainty += 1
print(certainty)