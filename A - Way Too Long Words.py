# https://codeforces.com/contest/71/problem/A
# Verdict: Accepted
# Memory: 0 KB
# Time: 109 ms
# CbyM
inp = int(input())
counter = 0
while inp != counter:
    counter += 1
    word = input()
    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print(word)