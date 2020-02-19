r1, c1, r2, c2 = map(int, input().split())
height = r2 - r1 + 1
width = c2 - c1 + 1

mat = [[0] * width for i in range(height)]
num = 1

repeat = 1
maxV = width * height

mat[0-r1][0-c1] = num
a = 0
b = 0  # 좌표

bigbreak = False

while (num < maxV):
    # 오른쪽 위쪽 왼쪽 아래
    for i in range(repeat):
        if num == maxV:
            break
        num += 1
        x = (b + 1 - c1)
        y = (a - r1)
        b += 1
        if(y < height and x < width):
            mat[y][x] = num

    for i in range(repeat):
        if num == maxV:
            break
        num += 1
        x = b - c1
        y = a - 1 - r1
        a -= 1
        if(y < height and x < width):
            mat[y][x] = num

    repeat += 1

    for i in range(repeat):
        if num == maxV:
            break
        num += 1
        x = b - 1 - c1
        y = a - r1
        b -= 1
        if(y < height and x < width):
            mat[y][x] = num

    for i in range(repeat):
        if num == maxV:
            break
        num += 1
        x = b - c1
        y = a+1 - r1
        a += 1
        if(y < height and x < width):
            mat[y][x] = num

    repeat += 1


for i in mat:
    for j in i:
        print(str(j).rjust(len(str(maxV)), ' '), end=' ')

    print()
