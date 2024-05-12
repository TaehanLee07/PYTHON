# 문자열 응용하기
# 문자열은 문자열을 조작하거나 정보를 얻는 다양한 메서드(method)를 제공합니다
# 다양한 메서드가 있지만 그중 자주 쓰는 메서드들을 알아봅시다.

# 1-1 문자열 바꾸기
# 문자열을 바꿀때는 replace('바꿀문자열', '새문자열') 를 사용합니다.
# 예제
str = 'Hello, Goodbye'
print(str.replace('Goodbye', 'Hello')) # 'Hello, Hello' 출력

# 1-2 문자열 분리하기
# split()은 공백을 기준으로 문자열을 분리하여 리스트로 만듭니다. 
# input으로 문자열을 입력받은 뒤 리스트로 만든 메서드가 바로 이 split입니다.
# 예제
a = 'apple ball cat dog elephant'.split()
print(a) # ['apple', 'ball', 'cat', 'dog', 'elephant'] 출력
# split('문자열') 이렇게 지정할 수도 있기에 공백을 기준으로 분리가 아닌 콤파(,)를 기준으로 분리할수도 있다.

# 1-3 대소문자 변경하기
# 이번에는 문자열의 문자를 대소문자로 바꾸는 방법입니다.
# upper()는 문자열의 문자를 모두 대문자로 바꿉니다 만약 대문자가 있으면 그대로 유지됩니다.
# lower()는 문자열의 문자를 모두 소문자로 바꿉니다. 만약 문자열 안에 소문자가 있다면 그대로 유지됩니다.
# 예제
print('hello, world'.upper()) # HELLO, WORLD
print('HELLO, WORLD'.lower()) # hello, world

# 1-4 공백 제거하기
# 문자열을 사용하다 보면 공백을 삭제해야 할 경우가 생깁니다. 이때는 lstrip, rstrip, strip 메서드를 사용합니다.
# lstrip()은 문자열에서 왼쪽에 있는 연속된 모든 공백을 삭제합니다 l은 left를 의미
# rstrip()은 문자열에서 오른쪽에 있는 연속된 모든 공백을 삭제합니다 r은 right를 의미
# strip()은 문자열에서 양쪽에 있는 모든 공백을 삭제합니다.
# 예제
print('         \'Python''\''.lstrip()) # 'Python'
print('\'Python''\'                     '.rstrip()) # 'Python'
print('         \'Python''\'        '.strip()) # 'Python'

# 1-5 특정 문자 삭제하기
# lstrip, rstrip, strip으로 공백뿐만이 아닌 strip('삭제할 문자들')을 넣어서 문자열에서 특정 문자를 삭제할 수 있다.
# 왼쪽의 특정 문자 삭제하기
# 예제
print(', python.'.lstrip(',.')) #  python.
# 오른쪽의 특정 문자 삭제하기
print(', python.'.rstrip(',.')) # , python
# 특정 문자 삭제하기
print(', python.'.strip(',.')) # python

# 2-1 문자열을 정렬하기
# 이번에는 문자열에 공백을 넣어서 원하는 위치에 정렬하는 방법을 알아보자
# 문자열을 왼쪽 정렬하기 ljust(길이)는 문자열을 지정된 길이로 만든 뒤 왼쪽으로 정렬하며 남는 공간을 공백으로 채웁니다
# 예제
print('taehan'.ljust(10) + '07') # 'taehan'    '07'

# 문자열을 오른쪽 정렬하기
print('python'.rjust(10) + 'java') #     'pythonjava'

# 문자열 가운데 정렬하기
print('python'.center(10)) #   'python'  

# 2-2 메서드 체이닝
# 문자열 메서드는 처리한 결과를 반환하도록 만들어져 있습니다. 따라서 메서드를 계속 연결해서 호출하는 메서드 체이닝이 가능합니다.
# 문자열을 오른쪽으로 정렬한 뒤 'py' 를 'ty' 로 변경하고 모두 대문자로 바꿔라 라고 하면.
# 예제
print('python'.rjust(10).replace('py','ty').upper()) #     'TYTHON' 출력
# 이런식으로 사용할 수 있다.

# 2-3 문자열 찾기
# find('찾을문자열')은 문자열에서 특정 문자열을 찾아서 인덱스를 반환하고, 문자열이 없으면 -1을 반환합니다.
# find는 왼쪽에서부터 문자열을 찾는데, 같은 문자열이 여러 개일 경우 처음 찾은 문자열의 인덱스를 반환합니다.
# 예제
print('babcdeagh'.find('a')) # 최초롤 발견된 a의 주소값 1 출력

# 오른쪽에서부터 문자열 위치 찾기
# find는 왼쪽에서 부터 찾지만 rfind는 오른쪽에서 부터 문자열을 찾는다
print('apapapa'.rfind('a')) # 가장 오른쪽에 있는 a의 주소값 6 출력

# 2-5 문자열 개수 세기
# count('문자열')은 현재 문자열에서 특정 문자열이 몇 번 나오는지 알아냅니다.
# 예제
print('abcdaaahijk'.count('a')) # a의 갯수인 4 출력
