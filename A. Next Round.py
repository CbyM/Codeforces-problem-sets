# https://codeforces.com/contest/158/problem/A
# Veredict: Accepted
# Memory: 16KB
# Time: 218 Ms
# CbyM

n, k = map(int, input().split())
a = map(int, input().split())
grades = list(a)
kth_place = grades[k-1]
advances = 0
for i in range(0, len(grades)):
    if grades[i] >= kth_place and grades[i] > 0:
        advances += 1
print(advances)
