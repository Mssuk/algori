import copy

# virus 2~ 10개. 세워야하는 벽 3개
f = open('D:/ALGORITHM/00_HOMEWORK/input.txt', 'r')
m, n = map(int, f.readline().split())

blank = [[0] * m for i in range(n)]
lab = copy.deepcopy(blank)
check = copy.deepcopy(blank)


def printMat():
    # print
    print("pan")
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            print(lab[i][j], end=' ')
        print()
    print("check")
    for i in range(len(check)):
        for j in range(len(check[i])):
            print(check[i][j], end=' ')
        print()


def catastro(x, y, opt):

    if x >= m or x < 0 or y >= n or y < 0:
        return

    if opt == 0 and check[x][y] != 0:
        return

    check[x][y] = 1

    if lab[x][y] == 1:
        return
    if lab[x][y] == 0:
        lab[x][y] = 2

    printMat()

    for i in dir:
        catastro(x+i[0], y+i[1], 0)


def count():
    cnt = 0
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if lab[i][j] == 0:
                cnt += 1
    return cnt

# virus 좌표
virus = []
# 2차원 배열 좌표
coord = []
# direction
dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]


for i in range(m):
    str = f.readline().split()
    for j in range(m):
        lab[i][j] = int(str[j])
        if lab[i][j] == 2:
            virus.append((i, j))
        coord.append((i, j))
f.close()

lab_2 = copy.deepcopy(lab)

# printMat()
maxV = 0

# 벽 3개 세우기
# for i in range(0, m * n):
#     coo = coord[i]
#     if lab[coo[0]][coo[1]] != 0:
#         continue
#     else:
#         lab[coo[0]][coo[1]] = 1
#     for j in range(i + 1, m * n):
#         coo2 = coord[j]
#         if lab[coo2[0]][coo2[1]] != 0:
#             continue
#         else:
#             lab[coo2[0]][coo2[1]] = 1
#         for k in range(j + 1, m * n):
#             coo3 = coord[k]
#             if lab[coo3[0]][coo3[1]] != 0:
#
#                 continue
#             else:
#                 lab[coo3[0]][coo3[1]] = 1
#                 for l in range(len(virus)):
#                     catastro(virus[l][0], virus[l][1], 1)
#                 maxV = max(maxV, count())
#                 lab = copy.deepcopy(lab_2)
#                 check = copy.deepcopy(blank)
#             lab[coo3[0]][coo3[1]] = 0
#         lab[coo2[0]][coo2[1]] = 0
#     lab[coo[0]][coo[1]] = 0


for l in range(len(virus)):
    catastro(virus[l][0], virus[l][1], 1)
    maxV = count()

print(maxV)
