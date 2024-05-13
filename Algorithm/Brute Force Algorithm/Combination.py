# 조합이란 경우의 수를 뜻합니다. A, B, C 3개의 음식이 있는데 친구와 2개를 주문하기로 하였습니다. 같이 먹기 위한 것으로 순서가 필요 없습니다
arr = ['A', 'B', 'C']
N = len(arr)

combs = []
for i in range(N - 1):
    for j in range(i + 1, N):
        combs.append((arr[i], arr[j]))

print(combs) # [('A', 'B'), ('A', 'C'), ('B', 'C')] 출력
