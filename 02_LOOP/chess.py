cnt = 25

# 2        -> 1*2 =2
# 3*1 2*2  -> 2*2 =4 = 2 + 2
# 3*2 2*3  -> 2*3 =6 = 4 + 2
# 4*2 3*3  -> 3*3 =9 = 6 + 3
# 4*3 3*4  -> 3*4 =12 = 9 + 3

x = 2
y = 1

for i in range(1, cnt):
    if (x+1) * (y) > (x) * (y+1):
        x = x+1
    else:
        y = y+1
print(x*y)


'''
N = int(input())
n = N//2
print((n+1)*(n+2) if N%2 else (n+1)**2)
'''
