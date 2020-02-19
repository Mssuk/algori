cnt = int(input())

a = 1
b = 0

for i in range(cnt):
    a, b = b, a+b

print(a, b)


'''
import sys
input = sys.stdin.readline
k = int(input())
a,b = 1,0
for _ in range(k):
    a,b = b,a+b
print(a,b)
'''
