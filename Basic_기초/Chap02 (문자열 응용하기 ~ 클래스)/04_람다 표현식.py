# 람다 표현식 사용하기
# 지금까지 def로 함수를 정의해서 사용해봤다. 이번에는 람다 표현식으로 익명 함수를 만드는 방법을 알아보자.

# 1-1 람다 표현식으로 함수 만들기
# 람다 표현식은 아래와 같이 만들수 있다.
# lambda 매개변수들: 식
# 예를 들어
def plus_ten(x):
  return x + 10
# 매개변수에 10을 더하는 간단한 함수를 람다 표현식으로 바꾸면
lambda x: x + 10
# 이렇게 된다 람다로 만든 함수를 출력하려면 변수에 할당해줘야 한다
a = lambda x: x + 10
a(1) # 11

# 1-2 람다 표현식 자체를 호출하기
# 람다 표현식은 변수에 할당하지 않고 람다 표현식 자체를 바로 호출할 수 있다. 다음과 같이 람다 표현식을 ( )(괄호)로 묶은 뒤에 다시 ( )를 붙이고 인수를 넣어서 호출하면 된다.
# (lambda 매개변수들: 식)(인수들)
a = (lambda x: x + 10)(1) # 11
print(a) # 11 출력

# 1-3 람다 표현식 안에서는 변수를 만들 수 없다
# 람다 표현식에서 주의할 점은 람다 표현식 안에서는 새 변수를 만들 수 없다는 점이다. 따라서 반환값 부분은 변수 없이 식 한 줄로 표현할 수 있어야 한다. 
(lambda x: y = 10; x + y)(1) # SyntaxError: invalid syntax

# 단, 람다 표현식 바깥에 있는 변수는 사용할 수 있다. 다음은 매개변수 x와 람다 표현식 바깥에 있는 변수 y를 더해서 반환해준다.
y = 10
(lambda x: x + y)(1) # 11

# 람다 표현식을 인수로 사용하기
# 람다 표현식을 사용하는 이유는 함수의 인수 부분에서 간단하게 함수를 만들기 위해서 입니다. 이런 방식으로 사용하는 대표적인 예가 map이다.
# def 로 map 작성
def plus_ten(x):
    return x + 10
print(list(map(plus_ten, [10, 20, 30]))) # [20, 30, 40] 출력

# 람다로 작성
print(list(map(lambda x: x + 10, [10, 20, 30]))) # [20, 30, 40] 출력

# 1-4 람다 표현식에 조건부 표현식 사용하기
# 사용법 : lambda 매개변수들: 식1 if 조건식 else 식2
# 한번 a에서 3의 배수를 문자열로 변환시키는 람다 함수를 만들어 보자
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a))) # [1, 2, '3', 4, 5, '6', 7, 8, '9', 10] 출력

# 1-5 map에 객체를 여러 개 넣기
# map은 리스트 등의 반복 가능한 객체를 여러 개 넣을 수도 있다.
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
print(list(map(lambda x, y: x * y, a, b))) # 두 리스트의 요소를 곱해서 새 리스트를 생성함. 리스트 : [2, 8, 18, 32, 50]

# 1-6 filter 사용하기
# filter는 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져오는데, filter에 지정한 함수의 반환값이 True일 때만 해당 요소를 가져옵니다.
# filter(함수, 반복가능한객체) 이렇게 사용할 수 있다.
# def 로 filter 사용 (리스트에서 5보다 크면서 10보다 작은 숫자를 가져옴)
def filter1(arr):
    return arr > 5 and arr < 10
# 람다 표현식
a = [1, 3, 2, 10, 15, 20, 15, 9, 0, 11]
list(filter(lambda x: x > 5 and x < 10, a))
