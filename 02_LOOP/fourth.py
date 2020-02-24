li = list(map(int, input().split()))

li.sort()
cha = 0
cha0 = li[-1] - li[-2]
cha1 = li[1] - li[0]

if cha0 > cha1:
    cha = cha1
else:
    cha = cha0

li2 = li[:]
dap = 0
for i in range(0, len(li) - 1):
    temp = li[i + 1] - li[i]
    if temp != cha:
        dap = li[i]+cha
        li2.insert(i+1, li[i] + cha)

if len(li2) != 4:
    dap = li2[-1] + cha

print(dap)
