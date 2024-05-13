# ​클래스는 객체를 표현하기 위한 문법입니다. 예를 들어 게임을 만든다고 하면 기사, 마법사, 궁수, 사제 등 직업별로 클래스를 만들어서 표현할 수 있습니다.

# 1-1 클래스와 메서드 만들기
# 클래스 예시
class 클래스이름:
    def 메서드(self):
        코드
class Person:
    def Hello(self):
        print('Hello')
p = Person() # 인스턴스 화
p.Hello() # 클래스에 있는 메서드 호출 'Hello 출력'

# 1-2 속성 사용하기
# 지금까지 클래스에서 메서드를 만들고 호출해보았죠?. 이번에는 클래스에서 속성을 만들고 사용해보겠습니다. 속성(attribute)을 만들 때는 __init__ 메서드 안에서 self.속성에 값을 할당합니다.
# 예시
class 클래스이름:
    def __init__(self):
        self.속성 = 값

class Person:
    def __init__(self):
        self.hello = '안녕하세요.'
    def Hello(self):
        print(self.hello)
lee = Person()
lee.Hello()  # 안녕하세요.
# __init__ 메서드는 james = Person()처럼 클래스에 ( )(괄호)를 붙여서 인스턴스를 만들 때 호출되는 특별한 메서드입니다. 이름 그대로 인스턴스(객체)를 초기화 합니다.
# 이렇게 앞뒤로 '_'가 두개가 붙는 메서드는 파이썬이 자동으로 호출해주는 메서드인데 이걸 스폐셜 메서드(special method) 또는 매직 메서드(magic method) 라고 합니다.

# 1-3 비공개 속성 사용하기
# 이 속성들은 메서드에서 self로 접근할 수 있고, 인스턴스.속성 형식으로 클래스 바깥에서도 접근할 수 있습니다.
class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
lee = Person('이태한', 18, '경기도 xx시')
print(lee.name, lee.age, lee.address) # 이태한 18 경기도 xx시 출력
# 이번에는 클래스 바깥에서는 접근할 수 없고 클래스 안에서만 사용할 수 있는 비공개 속성(private attribute)을 사용해보자.
# 비공개 속성은 ' __ '속성과 같이 이름이 ' __ ' 로 시작해야 합니다. 단, __속성__처럼 밑줄 두 개가 양 옆에 왔을 때는 비공개 속성이 아닙니다.
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

    def pay(self, amount):
        self.__wallet -= amount  # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print('잔액 {0}원'.format(self.__wallet))


lee = Person('이태한', 18, '서울시 xx구 xx동', 1000)
lee.pay(500) # 잔액 500원 출력

# 1-4 클래스 속성과 정적, 클래스 메서드 사용하기
# 클래스 속성 사용하기 
# 클래스 속성은 다음과 같이 클래스에 바로 속성을 만듭니다.
# 예시
class 클래스명:
    속성 = 값
# 이제 간단하게 사람 클래스에 클래스 속성으로 가방 속성과 가방안에 물건을 넣는 put_bag 메서드를 만들어 봅시다.
class Person:
    bag = []
    def put_bag(self, item):
        self.bag.append(item)
      
lee = Person()
lee.put_bag('과자')

park = Person()
park.put_bag('핸드폰')

print(lee.bag)
print(park.bag)
# 출력시 두개 모두다 책과 열쇠를 넣었다고 출력이된다 즉 클래스 속성은 클래스에 속해 있으며 모든 인스턴스에서 공유된다는 소리이다.

# 인스턴스 속성 사용하기
# 그럼 가방을 여러 사람이 공유하지 않으려면 어떻게 해야 하냐면? 그냥 bag을 인스턴스 속성으로 만들면 됩니다.
class Person:
    def __init__(self):
        self.bag = [] # bag 을 인스턴스 속성으로 만듬

    def put_bag(self, item):
        self.bag.append(item)

lee = Person()
lee.put_bag('과자')

park = Person()
park.put_bag('핸드폰')

print(lee.bag)
print(park.bag)
# 출력 ['과자'] ['핸드폰']
# 출력시 잘 분리 되어있는걸 볼수있다.

# 1-5 정적 메서드 사용하기
# 정적 메서드는 인스턴스를 통해 호출하는것이 아닌 바로 호출 가능한 메서드이다. 사용시에는 메서드 위에 @staticmethod를 붙혀서 사용합니다.그리고 매개변수엔 self 값이 저장되지 않습니다.
class number_calc:
    @staticmethod
    def num_add(a, b):
        print(a + b)

    @staticmethod
    def num_minus(a, b):
        print(a - b)

    @staticmethod
    def num_multiple(a, b):
        print(a * b)

    @staticmethod
    def num_div(a, b):
        print(a / b)        
number_calc.num_add(1,2) # 3 출력
number_calc.num_minus(5,3) # 2 출력
number_calc.num_multiple(2,3) # 6 출력
number_calc.num_div(10,2) # 5.0 출력  만약 소수점을 없애고 싶으면 print(int(a / b))를 사용해보자
# 이렇게 간단히 계산기 클래스를 만들보았다 클래스에서 바로 메서드 호출이 되는것을 볼 수 있다.

# 2-1 상속 사용하기
# 지금까지 클래스의 기본적인 사용 방법을 알아보았습니다. 이번에는 클래스 상속(inheritance)을 사용해보겠습니다.
# 상속은 무언가를 물려받는다는 뜻입니다. 그래서 클래스 상속은 물려받은 기능을 유지한채로 다른 기능을 추가할 때 사용하는 기능입니다. 
# 여기서 기능을 물려주는 클래스를 기반 클래스(base class), 상속을 받아 새롭게 만드는 클래스를 파생 클래스(derived class)라고 합니다.
# 기반 클래스는 부모 클래스, 슈퍼 클래스 라는 이름으로도 불리며 파생 클래스는 자식 클래스, 서브 클래스 라고도 불린다.
# 서람 클래스로 학생 클래스 만들기
# 예시
class 기반(부모)클래스이름:
    코드
 
class 파생클래스이름(기반클래스이름):
    코드

# 기반 클래스
class Person:
    def self_introduce(self):
        print('안녕하세요.')

# 파생 클래스 
class Student(Person): # 상속을 받아옴
    def study(self):
        print('공부하기')
    def go_school(self):
        print('학교가자 ㅜ')

lee = Student()
lee.self_introduce()  # 안녕하세요.: 기반 클래스 Person의 메서드 호출 사용가능
lee.study()  # 공부하기: 파생 클래스에 추가한 study 메서드
lee.go_school() # 학교가기 : 파생 클래스에 추가한 go_school 메서드

# 상속 관계 확인하기
# 클래스의 상속 관계를 확인하고 싶을 때는 issubclass 함수를 사용해서 알 수 있다. 클래스가 기반 클래스의 파생 클래스인지 확인하고. 기반 클래스의 파생 클래스가 맞으면 True, 아니면 False를 반환해준다.
print(issubclass(Student, Person)) # True
print(issubclass(Person, Student)) # False

# 2-2 상속 관계
# 앞에서 만든 Student 클래스는 Person 클래스를 상속받아서 만들어 졌다.
# 학생 Student는 사람 Person이므로 같은 종류이다. 이처럼 상속은 명확하게 같은 종류이며 동등한 관계일 때 사용한다. 즉, "학생은 사람이다."라고 했을 때 말이 되면 동등한 관계이고. 그래서 상속 관계를 영어로 is-a 관계라고 부릅니다(Student is a Person).
# 하지만 학생 클래스가 아니라 사람 목록을 관리하는 클래스를 만든다면 어떻게 해야 하나 그럴때는 리스트 속성에 Person 인스턴스를 넣어서 관리하면 해결된다.
class Person:
    def self_introduce(self):
        print('안녕하세요.')
      
class PersonList:
    def __init__(self):
        self.person_list = []  # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person):  # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)

# 2-3 기반 클래스의 속성 사용하기
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '성일정보고'

lee = Student()
print(lee.school)
print(lee.hello)  # 기반 클래스의 속성을 출력하려고 하면 에러가 발생함

# super()로 기반 클래스 초기화하기
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()  # super()로 기반 클래스의 __init__ 메서드 호출
        self.school = '성일정보고'

lee = Student()
print(lee.school)
print(lee.hello)  # 기반 클래스의 속성을 출력하려고 하면 에러가 발생함

# 기반 클래스를 초기화하지 않아도 되는 경우
# 만약 파생 클래스에서 __init__ 메서드를 생략한다면 기반 클래스의 __init__이 자동으로 호출되므로 super()는 사용하지 않아도 됩니다.

# 3-1 메서드 오버라이딩
# 오버라이딩(overriding)은 무시하다, 우선하다라는 뜻을 가지고 있는데 말 그대로 기반 클래스의 메서드를 무시하고 새로운 메서드를 만든다는 뜻입니다.
class Person:
    def Hello(self):
        print('안녕하세요.')
class Student(Person):
    def Hello(self):
        super().Hello()  # 기반 클래스의 메서드 호출하여 중복을 줄임
        print('저는 성일정보고 학생입니다.')
      
lee = Student() # 안녕하세요. 출력
lee.Hello() # 저는 성일정보고 학생입니다 출력

# 3-2 다중 상속 사용하기
# 사용법
class 파생클래스이름(기반클래스이름1, 기반클래스이름2):
    코드

class Person:
    def Hello(self):
        print('안녕하세요.')


class University:
    def manage_score(self):
        print('학점 관리')


class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

lee = Undergraduate()
lee.Hello()  # 기반 클래스 Person의 메서드 호출
lee.manage_score() # 학점 관리: 기반 클래스 University의 메서드 호출
lee.study()  # 파생 클래스 Undergraduate에 추가한 study 메서드
# 이렇게 하면 두 기반 클래스의 기능을 모두 상속받습니다.

# 3-3 다이아 몬드 상속
# 기반 클래스 A가 있고, B, C는 A를 상속받는다. 그리고 다시 D는 B, C를 상속받는다
class A:
    def Hello(self):
        print('안녕하세요. A입니다.')

class B(A):
    def Hello(self):
        print('안녕하세요. B입니다.')
      
class C(A):
    def Hello(self):
        print('안녕하세요. C입니다.')
      
class D(B, C):
    pass

a = D()
a.Hello()  # 안녕하세요. B입니다.

# 4-1 추상 클래스 사용 
# 파이썬은 추상 클래스(abstract class)라는 기능을 제공합니다. 추상 클래스는 메서드의 목록만 가진 클래스이며 상속받는 클래스에서 메서드 구현을 강제하기 위해 사용된다
# 사용시 import 로 abc 모듈을 가져와야 한다. abstract class 의 약자이다
from abc import *
 
class 추상클래스이름(metaclass=ABCMeta):
    @abstractmethod
    def 메서드이름(self):
        코드

from abc import *
class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')

lee = Student()
lee.study()
# 에러 발생 : 추상 클래스 StudentBase에서는 추상 메서드로 study와 go_to_school을 정의했습니다. 하지만 StudentBase를 상속받은 Student에서는 study 메서드만 구현하고, go_to_school 메서드는 구현하지 않았으므로 에러가 발생합니다.
# 따라서 추상 클래스를 상속받았다면 @abstractmethod가 붙은 추상 메서드를 모두 구현해야 합니다. 다음과 같이 Student에서 go_to_school 메서드도 구현해줍니다.

from abc import *


class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')

    def go_to_school(self):
        print('학교가기')

lee = Student()
lee.study()
lee.go_to_school() # 공부하기, 학교가기 출력

# 4-2 추상 메서드를 빈 메서드로 만드는 이유
# 추상 클래스는 인스턴스로 만들 수가 없기 떄문에 지금까지 추상 메서드를 만들 때 pass만 넣어서 빈 메서드로 만든 것이다.
