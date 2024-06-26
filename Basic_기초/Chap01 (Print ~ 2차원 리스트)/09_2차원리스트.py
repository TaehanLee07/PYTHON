# 2차원 리스트 사용하기
# 리스트를 사용할 때 한 줄로 늘어선 1차원 리스트를 사용했는데 이번에는 평면 구조의 2차원 리스트를 사용해봅시다.
# 2차원 리스트는 다음과 같이 가로 세로 형태로 이루어져 있으며 행(row)과 열(column) 모두 인덱스 번호와 같이 0부터 시작합니다.

# 2차원 리스트를 만들고 요소에 접근하기
# 2차원 리스트는 리스트 안에 리스트를 넣어서 만들 수 있으며 안쪽의 각 리스트는 ,(콤마)로 구분합니다.
# 리스트 = [[값, 값], [값, 값], [값, 값]]
a = [[1, 2], [3, 4], [5, 6]]
print(a) # [[1, 2], [3, 4], [5, 6]]
# 구분하기 쉽게 
# a = [[1, 2],
#      [3, 4],
#      [5, 6]] 이렇게 해도 됩니다.

# 2차원 리스트의 요소에 접근하기
# 2차원 리스트의 요소에 접근하거나 값을 넣을때는 리스트 뒤에 []를 두 번 사용하며 [ ] 안에 세로(row) 인덱스와 가로(column) 인덱스를 지정해주면 됩니다.
# 접근 시
# 리스트[세로인덱스][가로인덱스]
# 값 할당시
# 리스트[세로인덱스][가로인덱스] = 값
a = [[1, 2], [3, 4], [5, 6]]
print(a[0][1]) # 2출력 첫번째 줄의 두번째 요소를 가져오는것이니 2를 출력한다
# 값 할당
a[0][1] = 10
print(a[0][1]) # 10 출력

# 톱니형 리스트
# 파이썬 에서는 가로 크기가 일정한 사각형 리스트 말고도 가로의 크기가 불규칙한 톱니형리스트도 만들 수 있다.
a = [[1, 2],
     [7, 8, 9],
     [10],
     [33, 44],
     [2024],
     [10, 13, 2007]]
# 이런식으로 만들 수 있다.

# 2차원 튜플
# 2차원 리스틍와 마찬가지로 튜플안에 튜플을 넣는 방식 혹은 튜플 안에 리스트를 넣는 방식, 리스트 안에 튜플을 넣는 방식 등이 가능합니다.\
# 튜플 = ((값, 값), (값, 값), (값, 값))
# 튜플 = ([값, 값], [값, 값], [값, 값])
# 리스트 = [(값, 값), (값, 값), (값, 값)]
a = ((10, 20), (30, 40), (50, 60))    # 튜플 안에 튜플을 넣은 2차원 튜플
b = ([10, 20], [30, 40], [50, 60])    # 튜플 안에 리스트를 넣음
c = [(10, 20), (30, 40), (50, 60)]    # 리스트 안에 튜플을 넣음

# 사람이 알아보기 쉽게 출력하기
# 2차원 리스트를 출력해보면 일자로 쭉 출력될것이다 그런데 이렇게 말고 일자로가 아닌 사각형 모양 그대로 출력하려면 어떻게 해야할까?
# 정답은 pprint의 함수를 사용하면 된다 pprint는 간단히 말하면 "예쁘게 인쇄” 할 수 있는 기능이라고 생각하면 된다.
from pprint import pprint
a = [[10, 20], [30, 40], [50, 60]]
pprint(a, indent=2, width=15)
# indent는 들여쓰기 칸 수, width는 가로 폭을 의미한다 출력하면 사각형 형태로 잘 출력된다.
# [ [10, 20],
#  [30, 40],
#  [50, 60]]
