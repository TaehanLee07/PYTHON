# 이터레이터 사용하기
# 파이썬의 for 반복문에서 range(100)과 같이 사용되는 것은 사실은 연속된 숫자를 모두 만들어내는 것이 아니라, 0부터 99까지의 값을 차례대로 꺼낼 수 있는 이터레이터를 생성합니다. 
# 이렇게 생성된 이터레이터는 반복할 때마다 값을 하나씩 꺼내서 사용합니다. 이 방식은 성능 측면에서 이점을 가지며, 데이터가 많을 때 메모리를 효율적으로 사용할 수 있습니다. 이를 지연 평가(lazy evaluation)라고 합니다.
# 1-1 반복 가능한 객체 알아보기
# 객체가 반복 가능한 객체인지 알아보는 방법은 객체에 __iter__ 메서드가 들어있는지 확인해보면 됩니다. 다음과 같이 dir 함수를 사용하면 객체의 메서드를 확인할 수 있습니다.
[1, 2, 3].__iter__()
# <list_iterator object at 0x03616630>
# 리스트의 이터레이터를 변수에 저장한 뒤 __next__ 메서드를 호출해보면 요소를 차례대로 꺼낼 수 있습니다.
it = [1, 2, 3].__iter__()
it.__next__() # 1 출력
it.__next__() # 2 출력
it.__next__() # 3 출력
it.__next__() # 에러 발생

#  리스트뿐만 아니라 문자열, 딕셔너리, 세트도 __iter__를 호출하면 이터레이터가 나옵니다.
'Hello, world!'.__iter__()
<str_iterator object at 0x03616770>
