# 예외 처리 사용하기
# 예외(exception)란 코드를 실행하는 중에 발생한 에러를 뜻합니다. 다음과 같이 10을 어떤 값으로 나누는 함수 ten_div가 있을 때 인수에 따라 정상으로 동작하기도 하고 에러가 나기도 한다.
# 1-1 try except로 사용하기
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드

try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)
except:    # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.')

# 1-2 예외의 에러 메시지 받아오기
try:
    실행할 코드
except 예외 as 변수:
    예외가 발생했을 때 처리하는 코드

y = [10, 20, 30]
 
try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except ZeroDivisionError as e:                    # as 뒤에 변수를 지정하면 에러를 받아옴
    print('숫자를 0으로 나눌 수 없습니다.', e)    # e에 저장된 에러 메시지 출력
except IndexError as e:
    print('잘못된 인덱스입니다.', e)

# 출력 인덱스와 나눌 숫자를 입력하세요: 2 0 (입력) 숫자를 0으로 나눌 수 없습니다. division by zero

# 1-3 else와 finally 사용하기
# 예외가 발생하지 않았을 때 코드를 실행하는 else를 사용해보겠습니다. 다음과 같이 else는 except 바로 다음에 와야 하며 except를 생략할 수 없습니다.

try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
else:
    예외가 발생하지 않았을 때 실행할 코드

try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
else:                        # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)
# finally 사용
# 이번에는 예외 발생 여부와 상관없이 항상 코드를 실행하는 finally를 사용해보겠습니다. 특히 finally는 except와 else를 생략할 수 있습니다.
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
finally:
    예외 발생 여부와 상관없이 항상 실행할 코드

try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
else:                        # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)
finally:                     # 예외 발생 여부와 상관없이 항상 실행됨
    print('코드 실행이 끝났습니다.')
# 출력 
# 나눌 숫자를 입력하세요: 2 (입력)
# 5.0
# 코드 실행이 끝났습니다.
# 에러 출력
# 나눌 숫자를 입력하세요: 0 (입력)
# 숫자를 0으로 나눌 수 없습니다.
# 코드 실행이 끝났습니다.
