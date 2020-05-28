# https://codeforces.com/contest/118/problem/A
# Verdict: Accepted
# Time: 218 ms
# Memory: 12KB
# CbyM
userString = input()
lst = list(userString.lower())
vowels = ['A', 'a', 'O', 'o', 'U', 'u', 'E', 'e', 'I', 'i', 'Y', 'y']
word = ''
for i in lst:
    if i not in vowels:
        word += '.'
        word += i
print(word)