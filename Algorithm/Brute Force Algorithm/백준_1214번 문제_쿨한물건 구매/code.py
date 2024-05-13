import sys
input = sys.stdin.readline

def cool_item_buy(D, P, Q):
    if D % P == 0 or D % Q == 0: return D

    P, Q = max(P, Q), min(P, Q) # P > Q
    mx_P = D // P + 1
    answer = P * mx_P

    for i in range(mx_P-1, -1, -1): 
        div, mod = divmod((D - (i * P)), Q) # P*i를 제외한 비용을 Q로 나눈 몫 & 나머지 
        if mod == 0: return D 
        mn_i = (i * P) + ((div + 1) * Q) # i에 대한 최소 비용
        if answer == mn_i: break # answer가 반복되는 경우
        answer = min(answer, mn_i)

    return answer

if __name__ == '__main__':
    D, P, Q = map(int, input().split())
    result = cool_item_buy(D, P, Q)
    print(result)
