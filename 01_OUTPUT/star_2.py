cnt = int(input())
for i in range(cnt - 1, -1, -1):
    print(" " * i + "*" * (cnt - i))
