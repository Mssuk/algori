lis = []
trace = [0] * 1001
n = int(input())
arr = list(map(int, input().split()))
# 3 5 7 9 2 1 4 8


def findLIS(n):
    for i in range(n):
        # 만나는 수가 현재 배열에 저장된 마지막 수보다 클 때
        if i == 0 or arr[i] > lis[-1]:
            trace[arr[i]] = len(lis)
            lis.append(arr[i])
        else:  # 만나는 수가 현재 배열에 저장된 마지막 수보다 작을 때 (연속적인 증가 수열이 끝남)
            start = 0
            end = len(lis)
            idx = end
            while start < end:  # start<end 일때 binary search 종료
                mid = (start + end) // 2
                if lis[mid] >= arr[i]:
                    idx = min(idx, mid)
                    end = mid
                else:
                    start = mid + 1
            lis[idx] = arr[i]
            trace[arr[i]] = idx

    print(lis)
    print(arr)
    print(trace)
    cur = len(lis) - 1
    for i in range(len(trace)-1, -1, -1):
        if trace[i] == cur:
            lis[cur] = i
            cur -= 1
    return len(lis)


print(findLIS(n))
print(lis)
