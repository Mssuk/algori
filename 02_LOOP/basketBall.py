cnt = int(input())

dic = dict()

for j in [input() for i in range(cnt)]:
    if j[0] in dic:
        dic[j[0]] += 1
    else:
        dic[j[0]] = 1

str = ""
for k, v in dic.items():
    if(int(v) >= 5):
        str += k

if str != "":
    print(''.join(sorted(str)))
else:
    print('PREDAJA')
