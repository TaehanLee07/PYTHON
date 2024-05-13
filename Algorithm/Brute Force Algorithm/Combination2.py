# 조합을 사용하기 위해서는 combinations라는 내장 함수를 사용합니다. 이 함수는 itertools라는 파이썬 내장 패키지에 있습니다.
# 사용법
# combinations(리스트, 조합수)
  
from itertools import combinations

food = ['A', 'B', 'C']
print(list(combinations(arr, 2))) # [('A', 'B'), ('A', 'C'), ('B', 'C')]
