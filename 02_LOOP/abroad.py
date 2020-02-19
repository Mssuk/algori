# li = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
str = input()

for v in 'CAMBRIDGE':
    str = str.replace(v, '')

print(str)

# for elem in str:
#     if elem in 'CAMBRIDGE':
#         continue
#     else:
#         print(elem, end="")
