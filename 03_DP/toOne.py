# 1로 만들기
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

queue = []
mini = 1000000


def fun(num, cnt):

    if num == 1:
        return cnt

    if num % 3 == 0:
        queue.append(num//3)
    if num % 2 == 0:
        queue.append(num//2)
    queue.append(num - 1)

    global mini
    while queue:

        print(fun(queue.pop(0), cnt+1))


num = int(input())

print(fun(num, 0))
