s = [int(input()) for i in range(9)]

breaker = False
candi = []

for i in range(len(s)):
    hap = sum(s)
    dummy = []
    dummy.append(s[i])
    hap -= s[i]
    for j in range(i + 1, len(s)):
        hap -= s[j]
        if hap == 100:
            dummy.append(s[j])
            candi = dummy
            breaker = True
        else:
            hap += s[j]
            continue
    if breaker is True:
        break

for i in candi:
    s.remove(i)

for i in s:
    print(i)

'''
7
8
10
13
15
19
20
23
25'''

'''
from itertools import combinations

x = []
for i in range(9):
    x.append(int(input()))
for i in combinations(x, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break


//////////////////////////////////////

from itertools import permutations
arr = []
for i in range(9):
    arr.append(int(input()))
s = 0
l = permutations(arr, 7)
answer = False
for i in l:
    if answer == True:
        break
    if sum(i) == 100:
        for j in i:
            print(j)
            answer = True
'''
