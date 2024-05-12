# 딕셔너리 조작하기
# 1-1. 딕셔너리에 키-값 쌍 추가하기
# 딕셔너리에는 새로운 키-값 쌍을 추가할 수 있습니다. setdefault와 update를 사용한다.
# 예시
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')  # 키 'e'를 추가
print(x)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': None} 출력

# 1-2. 딕셔너리에서 키의 값 수정하기
# 딕셔너리에서 특정 키의 값을 수정하거나 새로운 키-값 쌍을 추가할 수 있습니다. update 메서드를 사용합니다.
# 예시
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(a=90)  # 키 'a'의 값을 90으로 수정
print(x)  # {'a': 90, 'b': 20, 'c': 30, 'd': 40} 출력

# 1-3. 딕셔너리에서 키-값 쌍 삭제하기
# 딕셔너리에서 특정 키-값 쌍을 삭제할 수 있습니다. pop과 del을 사용합니다.
# 예시
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.pop('a')  # 키 'a'의 값 삭제
print(x)  # {'b': 20, 'c': 30, 'd': 40} 출력

# 1-4. 딕셔너리에서 임의의 키-값 쌍 삭제하기
# 딕셔너리에서 임의의 키-값 쌍을 삭제할 수 있습니다. popitem을 사용합니다.
# 예시
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.popitem()  # 임의의 키-값 쌍 삭제
print(x)  # {'a': 10, 'b': 20, 'c': 30} # 출력

# 1-5. 딕셔너리의 모든 키-값 쌍을 삭제하기
# 딕셔너리의 모든 키-값 쌍을 삭제할 수 있습니다. clear 메서드를 사용합니다.
# 예시
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.clear()  # 모든 키-값 쌍 삭제
print(x)  # {} 빈 딕셔너리 출력

# 1-6. 딕셔너리에서 키의 값을 가져오기
# 딕셔너리에서 특정 키의 값을 가져올 수 있습니다. get 메서드를 사용합니다.
# 예시
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
value = x.get('a')  # 키 'a'의 값 가져오기
print(value)  # 10 출력

# 1-7. 딕셔너리에서 키-값 쌍을 모두 가져오기
# 딕셔너리의 키-값 쌍, 키, 값들을 가져올 수 있습니다. items, keys, values 메서드를 사용합니다.
# 예시
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.items())  # dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)]) 출력
print(x.keys())  # dict_keys(['a', 'b', 'c', 'd']) 출력
print(x.values())  # dict_values([10, 20, 30, 40]) 출력

# 1-8. 리스트와 튜플로 딕셔너리 만들기
# 리스트 또는 튜플로부터 딕셔너리를 생성할 수 있습니다. fromkeys 메서드를 사용합니다.
# 예시
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)  # 키 리스트로 딕셔너리 생성
print(x)  # {'a': None, 'b': None, 'c': None, 'd': None} 출력
