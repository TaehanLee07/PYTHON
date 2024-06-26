# 순열은 순서를 고려하여 나열하는 경우의 수를 뜻합니다. 조합의 예와 같이 A, B, C 3개의 음식이 있습니다. 친구와 각자 어떤 음식을 먹을지 고를 모든 경우의 수를 구하라고 합니다. 
# 이런 경우 내가 A를 먹고, 친구가 B를 먹는 경우와 내가 B를 먹고, 친구가 A를 먹는 경우는 다른 경우 입니다. 이렇게 같은 A, B를 선택하더라도 (A, B)와 (B, A)는 다른 경우로 선택하는 것을 순열 이라고 합니다.
# 조합에서는 j의 범위를 i + 1로 하여 i 번째 선택된 항목이 다시 선택 되지 않게 하였습니다. 하지만 순열에서는 (A, B)와 (B, A)가 다르기 때문에 j도 처음부터 반복문을 돌아야 합니다.
food = ['A', 'B', 'C']
N = len(food)

permutation = []
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        permutation.append((food[i], food[j]))

print(permutation) 
# [('A', 'B'), ('A', 'C'), ('B', 'A'), 
#  ('B', 'C'), ('C', 'A'), ('C', 'B')]
