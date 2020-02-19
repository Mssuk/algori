li = []
while True:
    try:
        li.append(int(input()))
    except EOFError:
        break
b = list(sorted(li, reverse=True))[:5]
print(sum(b))
for idx, val in enumerate(li):
    if val in b:
        print(idx+1, end=' ')
