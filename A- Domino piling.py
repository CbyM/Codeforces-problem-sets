# https://codeforces.com/problemset/problem/50/A
# Verdict: Accepted
# Time: 218 ms
# Memory: 20 KB
# CbyM

n, m = map(int, input().split())
if (n * m) % 2 == 0:
    print((n*m) // 2)
if (n * m) % 2 != 0:
    print((n * m) // 2)