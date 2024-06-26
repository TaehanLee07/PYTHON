# 지금까지는 변수 하나에 값 하나씩 저장을 해왔다 그러나 이렇게 계속하다보면 불편할때가 생길것이다
# 예를 들어 a에 30개의 값을 넣어야한다면 a1 ~ a30 까지 변수를 30개를 생성해야한다 이런 문제를 없애기 위해 리스트를 사용한다.
# 리스트 선언
a = [1, 2, 3, 4, 5]
print(a) # [1, 2, 3, 4, 5] 변수 통째로 출력

# 여러가지 자료형을 하나의 리스트에 집어넣을수도 있다.
person = ['홍길동', 25, 180, False]
print(person) # ['홍길동', 25, 180, False] 

# 빈 리스트 생성
a = []
print(a) # []

# range를 이용한 배열생성  range는 연속된 숫자를 생성하는데 range에 10을 지정하면 0부터 9까지 숫자를 생성합니다. 예를 들어 range(0, 10) 이면 0 부터 9까지만 한다.
a = list(range(5, 12)) # 5부터 11 까지의 배열 생성
print(a) # [5, 6, 7, 8, 9, 10, 11]
# 증감 사용하기
a = list(range(0, 10, 2)) # 0부터 10 까지 2씩 증가하며 배열 생성
print(a) # [[0, 2, 4, 6, 8]
# 만약 증가폭을 음수로 지정하면 해당 값만큼 숫자가 감소한다.
a = list(range(10, 0, -2)) # 10부터  0까지 2씩 감소하며 배열 생성
print(a) # [10, 8, 6, 4, 2]

# 튜플 사용하기
# 변수에 값을 저장할 때 ( )(괄호)로 묶어주면 튜플이 되며 각 값은 ,(콤마)로 구분해줍니다. (a, b, c) 또는, 괄호로 묶지 않고 값만 콤마로 구분해도 튜플이 됩니다 a, b, c
# 튜플은 저장된 요소를 변경, 추가, 삭제할 수도 없다 그럼 왜 만들었는지 궁금해지는데 이유는 간단하다. 튜플은 요소가 절대 변경되지 않고 유지되어야 할 때 사용한다 튜플의 값을 바꾸면 오류가 발생해서 실수를 줄일수 있다.
a = (1,2,3,4,5,10)
print(a) # (1, 2, 3, 4, 5, 10)
# ()로 묶지 않아도 된다
a = 1,2,3,4,5,10
print(a) # (1, 2, 3, 4, 5, 10)
# 리스트와 마찬가지로 다양한 자료형을 넣을수있다.
person = ('홍길동', 25, 180, False)
print(person)

# range를 사용하여 튜플 만들기
# 튜플 = tuple(range(값))
a = tuple(range(10))
print(a) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# range(시작 값, 끝 값) 을 넣어서 튜플 생성
a = tuple(range(0,5))
print(a) # (0, 1, 2, 3, 4)

# range(시작 값, 끝 값, 증가 값) 을 넣어서 튜플 생성
a = tuple(range(0,10, 2))
print(a) # (0, 2, 4, 6, 8)
