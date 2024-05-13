# 순열 내장함수 사용
# 조합과 마찬가지로 순열도 내장함수가있다 'permutation' 조합과 마찬가지로 itertools 에서 가져와 사용할 수 있다.
from itertools import permutations
food = ['A', 'B', 'C']

print(list(permutations(food, 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), 
#  ('B', 'C'), ('C', 'A'), ('C', 'B')]
