# https://codeforces.com/contest/263/problem/A
# Verdict: Accepted
# Memory: 16 KB
# Time: 218 ms
# CbyM

matrix = [
     [0,  1,  2,  3,  4],
     [0,  1,  2,  3,  4],
     [0,  1, 'X', 3,  4],
     [0,  1,  2,  3,  4],
     [0,  1,  2,  3,  4],
 ]
mvFromMid = [2,  1,  0,  1,  2]
for i in mvFromMid:
    x = list(input())
    if '1' in x:
        print(i + mvFromMid[x.index('1')//2])