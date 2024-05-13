import sys

def min_coin_count(change):
    coin_types = [500, 100, 50, 10] # 동정 배열 생성
    count = 0

    for coin in coin_types:
        count += change // coin
        change %= coin

    return count

# 거슬러 줘야 할 돈 N (10의 배수)
N = int(sys.stdin.readline())

# 최소 동전 개수 계산
result = min_coin_count(N)
print("거슬러 줘야 할 동전의 최소 개수:", result)
